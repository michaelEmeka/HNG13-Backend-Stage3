from pydantic_ai import Agent
from fastapi import Request, Depends
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from .settings import *
from .models import *
from datetime import datetime, timezone


@app.post("/a2a/agent/techwowAgent", status_code=200)
async def a2a_endpoint(
    request: Request, redis_client: redis.Redis = Depends(get_redis)
) -> JSONRPCResponse:
    """Main A2A endpoint"""

    session_storage = SessionStore(redis_client)

    body = await request.json()
    print(body)
    try:
        if body.get("jsonrpc") != "2.0" or "id" not in body:
            return JSONResponse(
                status_code=404,
                content={
                    "jsonrpc": "2.0",
                    "id": body.get("id"),
                    "error": {
                        "code": -32600,
                        "message": "Invalid Request: jsonrpc must be '2.0' and id is required"
                    }
                }
            )

        rpc_request = JSONRPCRequest(**body)

        if rpc_request.method == "message/send":
            messages = [rpc_request.params.message]
            config = rpc_request.params.configuration
            context_id = "acd16ccd-2551-4b3c-9374-76008a2a14ca"
        elif rpc_request.method == "execute":
            messages = rpc_request.params.message
            context_id = rpc_request.params.contextId
            task_id = rpc_request.params.taskId

        # checks if there's any message, and retrieve last else return None
        user_message = messages[-1] if messages else None

        if not user_message:
            raise ValueError("No message sent from user!")

        for part in user_message.parts:
            if part.kind == "text":
                user_text_message = part.text.strip()

        # user sent a message, thus save to memory cache
        user_message = A2AMessage(
            messageId=user_message.messageId,
            role="user",
            kind="message",
            parts=[MessagePart(kind="text", text=user_text_message)],
        )
        # save to redis cache
        await session_storage.save_messages(context_id, user_message)

        print(user_text_message)
        # Generate response from gemini LLM
        gemini_response = await agent.run(user_text_message)

        gemini_response = str(gemini_response.output)
        print(gemini_response)
        print("yh")

        gemini_message = A2AMessage(
            messageId=str(uuid4()),
            role="agent",
            kind="message",
            parts=[MessagePart(kind="text", text=gemini_response)],
        )

        # save to redis cache
        await session_storage.save_messages(context_id, gemini_message)

        response = JSONRPCResponse(
            jsonrpc="2.0",
            id=body.get("id"),
            result=TaskResult(
                id=str(user_message.taskId),
                contextId=str(context_id),
                status=TaskStatus(
                    state="input-required",
                    timestamp=datetime.now(timezone.utc).strftime(
                        "%Y-%M-%DT%H:%M:%S.%f"[:-3] + "Z"
                    ),
                    message=gemini_message,
                ),
                history=(
                    await session_storage.load_messages(context_id) if not None else []
                ),
                kind="task",
            ),
        )
        return response

    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "id": body.get("id") if "body" in locals() else None,
                "error": {
                    "code": -32603,
                    "message": "Internal error",
                    "data": {"details": str(e)},
                },
            },
        )
