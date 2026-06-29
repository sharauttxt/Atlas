import requests

from atlas.core.config import MODEL_NAME


def ask(prompt: str) -> str:
    response = requests.post(
        "http://127.0.0.1:11434/api/chat",
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]