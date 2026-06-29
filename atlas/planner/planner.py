import json

from atlas.ai.manager import ask


SYSTEM_PROMPT = """
Ты управляешь AI-агентом.

Если пользователь хочет открыть файл,
ответь ТОЛЬКО JSON.

Пример:

{
    "tool":"read_file",
    "filename":"README.md"
}

Если инструмент не нужен:

{
    "tool":"chat"
}

Никакого текста кроме JSON.
"""


class Planner:

    def plan(self, text: str):

        prompt = SYSTEM_PROMPT + "\n\nПользователь:\n" + text

        response = ask(prompt)

        try:
            return json.loads(response)

        except Exception:

            return {
                "tool": "chat"
            }