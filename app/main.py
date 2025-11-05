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
):
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

        rpc_request = A2ARequest(**body)

        if rpc_request.method == "message/send":
            messages = [rpc_request.params.message]
            print(messages)
            config = rpc_request.params.configuration
            context_id = uuid4()

        # checks if there's any message, and retrieve last else return None
        user_message = messages[-1] if messages else None
        task_id = str(uuid4()) #user_message.taskId

        if not user_message:
            raise ValueError("No message sent from user!")

        for part in user_message.parts:
            if part.kind == "text":
                user_text_message = part.text.strip()

        # user sent a message, thus save to memory cache
        user_message_s = Message(
            messageId=user_message.messageId,
            role="user",
            kind="message",
            parts=[MessagePart(kind="text", text=user_text_message)],
            taskId=task_id
        )
        # save to redis cache
        await session_storage.save_messages(context_id, user_message_s)

        print(user_text_message)
        # Generate response from gemini LLM
        gemini_response = await agent.run(user_text_message)

        gemini_response = str(gemini_response.output)

        print(gemini_response)
        print("yh")

        gemini_message = Message(
            messageId=str(uuid4()),
            role="agent",
            parts=[MessagePart(kind="text", text=gemini_response)],
            kind="message",
            taskId=task_id
        )

        # save to redis cache
        await session_storage.save_messages(context_id, gemini_message)

        # print("taskid: ", str(user_message.taskId))

        response = A2AResponse(
            jsonrpc="2.0",
            id=body.get("id"),
            result=TaskResult(
                id=str(task_id),
                contextId=str(context_id),
                status=Status(
                    state="input-required",
                    timestamp=datetime.now(timezone.utc).strftime(
                        "%Y-%m-%dT%H:%M:%S.%f"
                    )[:-3]
                    + "Z",
                    message=gemini_message,
                    kind="message",
                ),
                artifacts=[
                    Artifact(
                        artifactId=str(uuid4()),
                        name="subjectMatter",
                        parts=[
                            DataPart(
                                kind="data",
                                data={
                                    "type": "fact",
                                    "heading": str(
                                        f"{gemini_response.split('.')[0][:60].strip()}..."
                                    ),
                                    "description": str(gemini_response.strip()),
                                    "category": "General Tech",
                                },
                            )
                        ],
                    )
                ],
                history=(
                    await session_storage.load_messages(context_id) if not None else []
                ),
                kind="task",
            ),
        )

        response = response.model_dump(exclude_none=True, exclude_unset=True)
        # response["result"]["status"]["message"].pop("taskId")

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
