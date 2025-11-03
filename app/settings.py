from fastapi import FastAPI
from pydantic_ai import Agent
from uuid import uuid4
from dotenv import load_dotenv

from .models import A2AMessage
from typing import List, Optional
import redis.asyncio as redis
import json
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()


app = FastAPI()
agent = Agent(
    "google-gla:gemini-2.0-flash",
    instructions="""
    You are a useful, interesting, and wow-inducing tech facts provider. 
    Your purpose is to share unknown, hidden, or mind-blowing facts about people, inventions, or discoveries in the tech world — from both past and present events.

    - Always begin by asking the user what topic they are interested in.
    - If the topic provided is not in English, automatically translate it to English before continuing.
    - When presenting a fact, include:
        • The name (of the person, invention, or discovery)
        • The date or time period
        • The contribution or discovery
        • The impact or why it’s remarkable
    - Keep your responses concise but insightful, ideally within 2–5 sentences.
    - If a user asks for something outside this mission, politely remind them that your sole purpose is to share fascinating tech facts. 
    If they insist, assist them briefly but return to your primary role afterward.
    - Always mention that you can also suggest a random tech topic if they have none in mind.

    """,
)

app = FastAPI()


# Create a single Redis connection
async def get_redis():

    client = await redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)
    print(await client.ping())
    try:
        yield client
    finally:
        await client.close()


class SessionStore:
    def __init__(self, redis_client: redis.Redis):
        # self.redis = redis.from_url(redis_url)
        self.redis: redis.Redis = redis_client

        # self.redis.ping

    async def save_messages(self, context_id: str, message: A2AMessage):
        key = f"convo: {context_id}"

        current_context_raw = await self.redis.get(key)
        if current_context_raw:
            current_context = json.loads(current_context_raw)
        else:
            current_context = []

        current_context.append(message.model_dump())

        await self.redis.set(key, json.dumps(current_context), ex=3600)  # 1 hour expiry

    async def load_messages(self, context_id: str) -> Optional[List[A2AMessage]]:

        messages_raw = await self.redis.get(f"convo: {context_id}")

        if not messages_raw:
            return None

        messages = json.loads(messages_raw)

        return [A2AMessage(**m) for m in messages]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
