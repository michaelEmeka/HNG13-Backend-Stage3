from uuid import uuid4

print(uuid4())


dic = {
    "jsonrpc": "2.0",
    "id": "26e44d32-fff9-437a-bc4d-c1f2d287be23",
    "result": {
        "id": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
        "contextId": "acd16ccd-2551-4b3c-9324-76008a2a14ca",
        "status": {
            "state": "completed",
            "timestamp": "2025-50-11/03/25T11:50:57Z",
            "message": {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some fascinating tech facts. What topic are you interested in today? We can dive into people, inventions, or discoveries, from past to present.\n\nIf you don't have a specific topic in mind, I can also suggest a random one!",
                    }
                ],
                "messageId": "bbb439e2-8b26-4955-a5dd-45580200ce1e",
                "taskId": None,
            },
        },
        "artifacts": [
            {
                "artifactId": "f782ad28-a23d-45d7-a35f-839407c98514",
                "name": "subjectMatter",
                "parts": [{"kind": "data", "data": {"heading": "Hello! I'm..."}}],
            }
        ],
        "history": [
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello there! I'm here to share some fascinating, little-known, or mind-blowing facts about people, inventions, or discoveries in the tech world.\n\nWhat tech topic are you curious about today? If you don't have one in mind, I can always suggest a random tech topic!",
                    }
                ],
                "messageId": "90d6e10b-6aff-4056-a567-04fa0c00f754",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some fascinating tech facts. What specific topic in the world of technology, past or present, are you curious about today?\n\nI can tell you about people, inventions, or discoveries. If you don't have a specific topic in mind, I can also suggest a random one!",
                    }
                ],
                "messageId": "a0539601-c47c-4a4a-8c8a-c2d45bfe7807",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating tech facts. What specific topic are you interested in today?\n\nI can tell you about a person, an invention, or a discovery. If you don't have a particular topic in mind, I can also suggest a random tech fact!",
                    }
                ],
                "messageId": "b7cb4d96-29f6-4fbd-88ee-499e02fc2c3f",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! What fascinating tech topic are you interested in today? I can share some unknown, hidden, or mind-blowing facts.\n\nIf you don't have a specific topic in mind, I can also suggest a random one!",
                    }
                ],
                "messageId": "54528d46-518f-4399-a3f4-22c044abebb9",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello there! What fascinating tech topic are you curious about today? I can share some unknown, hidden, or mind-blowing facts about people, inventions, or discoveries.\n\nIf you don't have a specific topic in mind, I can also suggest a random one!",
                    }
                ],
                "messageId": "59f0b476-dace-4b67-9c7b-eaef18750311",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating and often unknown facts about the world of technology.\n\nWhat topic are you interested in today? We can dive into a specific person, invention, or discovery. If you don't have one in mind, I can also suggest a random tech topic for you!",
                    }
                ],
                "messageId": "1b141b15-3fd1-4b16-85b0-17a8dfbef50f",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating tech facts. What person, invention, or discovery in the tech world are you curious about today?\n\nIf you don't have a specific topic in mind, I can also suggest a random one for you!",
                    }
                ],
                "messageId": "c20c46de-c609-4241-b436-1f4de73ee2e4",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating tech facts. What topic are you interested in today?\n\nI can also suggest a random tech topic if you have none in mind!",
                    }
                ],
                "messageId": "3fe1ad57-34ac-482f-bd5c-356ec7b2eade",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! What tech topic are you curious about today? I can also suggest a random one if you'd like!",
                    }
                ],
                "messageId": "aa5cb915-4c3e-4346-83b6-1a6ae157a37b",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating, unknown, or mind-blowing tech facts. What topic are you interested in today?\n\nI can also suggest a random tech topic if you have none in mind!",
                    }
                ],
                "messageId": "178ea4e8-cb7c-476b-a229-a1f806914934",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some truly fascinating and often unknown tech facts. What topic are you interested in today? We could delve into a specific person, an invention, or a discovery.\n\nI can also suggest a random tech topic if you have none in mind!",
                    }
                ],
                "messageId": "4ed24f9f-1b2e-46fd-97cb-23133dd271db",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some fascinating tech facts. What tech topic are you interested in today?\n\nI can also suggest a random tech topic if you have none in mind!",
                    }
                ],
                "messageId": "f831fbbd-ffe4-4cc7-90e0-447360b7f360",
                "taskId": "None",
            },
            {
                "kind": "message",
                "role": "user",
                "parts": [{"kind": "text", "text": "Hi"}],
                "messageId": "3a3d28c2-4796-4b1c-b8f8-223543a14b80",
                "taskId": "e62edcfd-b1f7-4a3b-a3e9-80288c82210f",
            },
            {
                "kind": "message",
                "role": "agent",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Hello! I'm here to share some fascinating tech facts. What topic are you interested in today? We can dive into people, inventions, or discoveries, from past to present.\n\nIf you don't have a specific topic in mind, I can also suggest a random one!",
                    }
                ],
                "messageId": "bbb439e2-8b26-4955-a5dd-45580200ce1e",
                "taskId": "None",
            },
        ],
        "kind": "task",
    },
}
print(dic["result"]["status"]["message"].pop("taskId"))
print(dic)
