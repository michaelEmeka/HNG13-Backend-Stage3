from pydantic import BaseModel, Field
from typing import List, Optional, Union, Any, Literal
from datetime import datetime


# ---------- COMMON PARTS ----------



class DataPart(BaseModel):
    kind: str = "dict"
    data: dict

class MessagePart(BaseModel):
    kind: str = "str"
    text: str

class Message(BaseModel):
    kind: str = "message"
    role: str  # "user" | "agent"
    parts: List[MessagePart]
    messageId: str
    taskId: Optional[str] = None


# ---------- REQUEST SCHEMA ----------


class Configuration(BaseModel):
    blocking: bool = True


class MessageParams(BaseModel):
    message: Message
    configuration: Optional[Configuration] = None


class StatusMessage(BaseModel):
    messageId: str
    role: str
    parts: List[MessagePart]
    kind: str = "message"


class Status(BaseModel):
    state: Literal["completed", "input-required", "canceled", "failed"] # e.g. "completed
    timestamp: str
    message: Message


class Artifact(BaseModel):
    artifactId: str
    name: str
    parts: List[DataPart]


class A2ARequest(BaseModel):
    jsonrpc: str = "2.0"
    id: str
    method: str  # e.g. "message/send"
    params: MessageParams
    artifacts: List[Artifact] = None


class TaskResult(BaseModel):
    id: str
    contextId: str
    status: Status
    artifacts: Optional[List[Artifact]] = None
    history: Optional[Any] = None  # You can refine later
    kind: str = "task"


class A2AResponse(BaseModel):
    jsonrpc: str = "2.0"
    id: str
    result: TaskResult