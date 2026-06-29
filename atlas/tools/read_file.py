from pathlib import Path

from atlas.executor.result import ToolResult
from atlas.tools.registry import register


class ReadFileTool:

    name = "read_file"

    def execute(self, filename: str):

        workspace = Path.cwd() / "workspace"

        matches = list(workspace.rglob(filename))

        if not matches:
            return ToolResult(
                success=False,
                tool="read_file",
                error="Файл не найден."
            )

        content = matches[0].read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return ToolResult(
            success=True,
            tool="read_file",
            output=content
        )


register(ReadFileTool())