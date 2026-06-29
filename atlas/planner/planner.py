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

Если пользователь просит создать, написать или сгенерировать файл,
ты ОБЯЗАН использовать инструмент write_file.

Поле "content" должно содержать ПОЛНОЕ содержимое файла.

Например:

Пользователь:
Создай hello.py

Ответ:

{
    "tool": "write_file",
    "filename": "hello.py",
    "content": "print('Hello World')"
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
    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    print("\n===== PLAN =====")
    print(response)
    print("================\n")

    try:
        data = json.loads(response)
        return data

    except Exception:
        return {
            "tool": "chat"
        }