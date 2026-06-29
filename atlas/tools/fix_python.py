from atlas.ai.manager import ask
from atlas.executor.result import ToolResult
from atlas.tools.registry import register


class FixPythonTool:

    name = "fix_python"

    def execute(self, code: str, error: str):

        prompt = f"""
Исправь Python-код.

Верни ТОЛЬКО исправленный код.

Ошибка:

{error}

Код:

{code}
"""

        fixed = ask(prompt)

        return ToolResult(
            success=True,
            tool="fix_python",
            output=fixed
        )


register(FixPythonTool())