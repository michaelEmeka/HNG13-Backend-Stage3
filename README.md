# TechWow AI Agent API

TechWow is an insightful and educative AI agent that gives interesting fun facts in the world of Tech. It’s a fairly simple agent as the project task requires.

A FastAPI-based backend service that provides interesting and wow-inducing tech facts through an A2A (Agent-to-Agent) interface. The service uses Google's Gemini 2.5 Flash model to generate engaging responses about technology, inventions, and discoveries.

## Features

-   🤖 AI-powered tech facts generation
-   💬 Conversational memory with Redis
-   🌐 A2A (Agent-to-Agent) communication protocol

# TechWow Agent API

A small FastAPI backend that exposes the TechWow AI agent via an A2A (Agent-to-Agent) JSON-RPC-style endpoint. The service uses a hosted LLM (configured in `app/settings.py`) to generate concise tech facts and preserves conversational context in Redis.

## Table of contents

-   [Features](#features)
-   [Tech stack](#tech-stack)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Running the server](#running-the-server)
-   [API](#api)
    -   [Request format](#request-format)
    -   [Response format](#response-format)
    -   [Error format](#error-format)
-   [Models reference (summary)](#models-reference-summary)
-   [Development](#development)
-   [Contributing](#contributing)
-   [License](#license)

## Features

-   🤖 AI-powered tech facts generation (via configured LLM)
-   💬 Conversation memory stored in Redis
-   🌐 JSON-RPC 2.0-style A2A request/response wrapper
-   🔒 CORS enabled for broad client support

## Tech stack

-   FastAPI
-   Redis (async client)
-   Pydantic (models & validation)
-   Python 3.10+

## Prerequisites

-   Python 3.10 or newer
-   Redis instance (local or hosted)
-   Environment variables (see below)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/michaelEmeka/HNG13-Backend-Stage3.git
cd HNG13-Backend-Stage3
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate   # macOS / Linux
# On Windows (PowerShell): .\env\Scripts\Activate.ps1
# On Windows (cmd): .\env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add environment variables: create a `.env` file in the repo root with at minimum:

```env
REDIS_URL=redis://localhost:6379/0
# (Add any provider-specific credentials required by your LLM client)
```

## Running the server

Start a development server with hot-reload:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API

Base endpoint:

```
POST /a2a/agent/techwowAgent
```

### Request format

Requests follow a JSON-RPC 2.0-style envelope. The request body must conform to the `A2ARequest` Pydantic model (see models summary below).

Example request (message/send):

```json
{
    "jsonrpc": "2.0",
    "id": "request-id-123",
    "method": "message/send",
    "params": {
        "message": {
            "messageId": "msg-1",
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "Tell me a cool tech fact about Ada Lovelace."
                }
            ],
            "taskId": "task-1"
        }
    }
}
```

### Response format

Successful responses follow a JSON-RPC 2.0-style envelope and use the `A2AResponse` model. The `result` is a `TaskResult` that contains `status`, optional `artifacts`, and optional `history`.

Example successful response (trimmed):

```json
{
    "jsonrpc": "2.0",
    "id": "request-id-123",
    "result": {
        "id": "task-1",
        "contextId": "acd16ccd-2551-4b3c-9324-76008a2a14ca",
        "status": {
            "state": "input-required",
            "timestamp": "2025-11-05T12:34:56.123Z",
            "message": {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Ada Lovelace wrote the first algorithm intended for a machine..."
                    }
                ],
                "messageId": "agent-msg-1",
                "taskId": null
            }
        },
        "artifacts": [
            {
                "artifactId": "artifact-1",
                "name": "subjectMatter",
                "parts": [
                    {
                        "kind": "data",
                        "data": { "heading": "Ada Lovelace fact" }
                    }
                ]
            }
        ],
        "history": [
            /* optional list of Message objects */
        ],
        "kind": "task"
    }
}
```

Notes:

-   `result.history` may be `null` or omitted; when present it contains an array of `Message` objects representing prior messages (the project stores/retrieves these from Redis in `SessionStore`).
-   `artifacts` is optional and contains `Artifact` objects built from `DataPart` entries.
-   Timestamps are serialized as strings; the current code uses UTC timestamps formatted when constructing responses.

### Error format

If a request is invalid or an internal error occurs, the endpoint returns a JSON-RPC-style error object. Example:

```json
{
    "jsonrpc": "2.0",
    "id": "request-id-123",
    "error": {
        "code": -32600,
        "message": "Invalid Request: jsonrpc must be '2.0' and id is required"
    }
}
```

## Models reference (summary)

See `app/models.py` for full Pydantic definitions. Brief summary:

-   `A2ARequest` — JSON-RPC envelope with `id`, `method`, and `params` (contains a `Message`).
-   `Message` — `messageId`, `role` (`user` | `agent`), `parts` (list of `MessagePart`), optional `taskId`.
-   `MessagePart` — `kind` (`text`|`data`), `text` (optional) or `data` (optional array of dicts).
-   `A2AResponse` — JSON-RPC envelope with `result` (a `TaskResult`).
-   `TaskResult` — `id`, `contextId`, `status` (`Status`), optional `artifacts`, optional `history`.
-   `Status` — `state` (`completed`|`input-required`|`canceled`|`failed`), `timestamp` (string), `message` (`Message`).

## Development

-   Redis is used to persist a rolling conversation history per `contextId` (see `SessionStore` in `app/settings.py`).
-   The Agent is configured in `app/settings.py` (the `agent` instance and its instructions). Adjust the model name and credentials there if needed.

## Contributing

Please open issues or PRs. Recommended workflow:

1. Fork the repo
2. Create a topic branch
3. Commit with a descriptive message
4. Open a PR against `main`

## License

MIT — see the `LICENSE` file for details.

-   `TaskResult`:

    -   `id` (str): task id
    -   `contextId` (str): conversation context id
    -   `status` (Status): task status and timestamp
    -   `artifacts` (Optional[list of Artifact]): optional data blobs
    -   `history` (Optional[Any]): conversation history (list of `Message` objects)

-   `Status`:

    -   `state` (one of: `completed`, `input-required`, `canceled`, `failed`)
    -   `timestamp` (str): ISO-like timestamp string
    -   `message` (Message): the agent or user message associated with the status

-   `Message` and `MessagePart`:
    -   `Message` includes `messageId`, `role` (`user` | `agent`), optional `taskId`, and `parts` (list of `MessagePart`).
    -   `MessagePart` has `kind` (`text` or `data`) and either `text` (string) or `data` (list of data dicts).

Example successful response (trimmed):

```json
{
    "jsonrpc": "2.0",
    "id": "request-id",
    "result": {
        "id": "task-id",
        "contextId": "acd16ccd-2551-4b3c-9324-76008a2a14ca",
        "status": {
            "state": "input-required",
            "timestamp": "2025-11-05T12:34:56.123Z",
            "message": {
                "kind": "message",
                "role": "agent",
                "parts": [{ "kind": "text", "text": "Here is a tech fact..." }],
                "messageId": "...",
                "taskId": null
            }
        },
        "artifacts": [
            {
                "artifactId": "...",
                "name": "subjectMatter",
                "parts": [
                    { "kind": "data", "data": { "heading": "Hello! I'm..." } }
                ]
            }
        ],
        "history": [
            /* list of Message objects */
        ],
        "kind": "task"
    }
}
```

Notes:

-   The `history` field may be `null` or omitted; when present it should be an array of `Message` objects matching the `Message` model in `app/models.py`.
-   `artifacts` contains `Artifact` objects with `DataPart` entries for any structured data the agent attaches.
-   Timestamps are stored as strings (the code currently uses `datetime.now(timezone.utc).strftime(...)` when building responses).
