import json

from atlas.ai.manager import ask


SYSTEM_PROMPT = """
Ты управляешь AI-агентом.

Ты должен отвечать ТОЛЬКО JSON.

Доступные инструменты:

1. read_file

Пример:

{
    "tool":"read_file",
    "filename":"main.py"
}

2. write_file

Пример:

{
    "tool":"write_file",
    "filename":"main.py",
    "content":"print('Hello')"
}

3. list_files

Пример:

{
    "tool":"list_files"
}

4. run_python

Пример:

{
    "tool":"run_python",
    "filename":"main.py"
}

Если инструмент не нужен:

{
    "tool":"chat"
}

Никакого текста.
Только JSON.
"""


class Planner:

    def plan(self, text: str):

    prompt = SYSTEM_PROMPT + "\n\nПользователь:\n" + text

    response = ask(prompt)

    print("\n===== PLAN =====")
    print(response)
    print("================\n")

    try:
        data = json.loads(response)

        if "steps" in data:
            return data

    except Exception:
        pass

    return {
        "steps": [
            {
                "tool": "chat",
                "text": text,
            }
        ]
    }