from pathlib import Path

from atlas.tools.registry import register


class ReadFileTool:

    name = "read_file"

    def execute(self, filename):
        print("ReadFileTool загружен")

        workspace = Path.cwd() / "workspace"

        matches = list(workspace.rglob(filename))

        if not matches:
            return "Файл не найден."

        return matches[0].read_text(
            encoding="utf-8",
            errors="ignore"
        )


register(ReadFileTool())