from openai import OpenAI
from atlas.core.config import OPENROUTER_API_KEY, MODEL_NAME

if not OPENROUTER_API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY не найден. Проверь файл .env"
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


def ask(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content.strip()