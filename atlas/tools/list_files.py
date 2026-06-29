from pathlib import Path

from atlas.executor.result import ToolResult
from atlas.tools.registry import register


class ListFilesTool:

    name = "list_files"

    def execute(self):

        workspace = Path.cwd() / "workspace"

        if not workspace.exists():
            return ToolResult(
                success=False,
                tool="list_files",
                error="Папка workspace не найдена."
            )

        files = []

        for path in workspace.rglob("*"):
            if path.is_file():
                files.append(str(path.relative_to(workspace)))

        if not files:
            return ToolResult(
                success=False,
                tool="list_files",
                error="В workspace нет файлов."
            )

        return ToolResult(
            success=True,
            tool="list_files",
            output="\n".join(files)
        )


register(ListFilesTool())