from fastapi import FastAPI
from pydantic_ai import Agent
from uuid import uuid4
from dotenv import load_dotenv

from .models import A2AMessage
from typing import List, Optional
import redis.asyncio as redis
import json
import os

load_dotenv()


app = FastAPI()
agent = Agent(
    "google-gla:gemini-2.0-flash",
    instructions="""
    You are a useful interesting, wow tech facts provider that provides unknown or hidden facts attributed to a person, invention or discovery in the tech world, based on present, or past events.
    Your primary function is to provide users with useful tech facts, hidden secrets or mind blowing did you know?'s
    
    -Always ask for a what topic the user is interested in\n
    - If the topic of interest isn't in English, please translate it\n 
    - Include relevant details like name, date, contribution, impact\n
    - Keep responses concise but informative\n
    - If the user asks for anything outside related to this mission, kindly remind user your sole purpose in a nice manner, if insist, help in the most brief way.
    -Always let the user know you can also suggest a random option
    """
)

app = FastAPI()


# Create a single Redis connection
async def get_redis():

    client = await redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)
    try:
        yield client
    finally:
        await client.close()


class SessionStore:
    def __init__(self, redis_client: redis.Redis):
        #self.redis = redis.from_url(redis_url)
        self.redis : redis.Redis = redis_client
        
        #self.redis.ping

    async def save_messages(self, context_id: str, message: A2AMessage):
        key = f"convo: {context_id}"
        
        current_context_raw = await self.redis.get(key)
        if current_context_raw:
            current_context = json.loads(current_context_raw)
        else:
            current_context = []
            
        current_context.append(message.model_dump())
        
        await self.redis.set(key
            , json.dumps(current_context), ex=3600  # 1 hour expiry
        )

    async def load_messages(self, context_id: str) -> Optional[List[A2AMessage]]:
        
        messages_raw = await self.redis.get(f"convo: {context_id}")
        
        if not messages_raw:
            return None
        
        messages = json.loads(messages_raw)
        
        return [A2AMessage(**m) for m in messages]
