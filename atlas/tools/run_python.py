from pathlib import Path
import subprocess

from atlas.executor.result import ToolResult
from atlas.tools.registry import register


class RunPythonTool:

    name = "run_python"

    def execute(self, filename: str):

        workspace = Path.cwd() / "workspace"

        path = workspace / filename

        if not path.exists():
            return ToolResult(
                success=False,
                tool="run_python",
                error="Файл не найден."
            )

        result = subprocess.run(
            ["python", str(path)],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            return ToolResult(
                success=True,
                tool="run_python",
                output=result.stdout or "Программа выполнена."
            )

        return ToolResult(
            success=False,
            tool="run_python",
            error=result.stderr
        )


register(RunPythonTool())