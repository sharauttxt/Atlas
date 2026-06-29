from pathlib import Path

from atlas.executor.result import ToolResult
from atlas.tools.registry import register


class WriteFileTool:

    name = "write_file"

    def execute(self, filename: str, content: str):

        workspace = Path.cwd() / "workspace"

        workspace.mkdir(exist_ok=True)

        path = workspace / filename

        path.write_text(
            content,
            encoding="utf-8"
        )

        return ToolResult(
            success=True,
            tool="write_file",
            output=f"Файл {filename} успешно сохранён."
        )


register(WriteFileTool())