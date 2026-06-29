from pathlib import Path


class WriteFileTool:

    def execute(self, filename, content):

        workspace = Path.cwd() / "workspace"

        path = workspace / filename

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return f"{filename} сохранён."