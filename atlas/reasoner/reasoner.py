from atlas.executor.result import ToolResult


class Reasoner:

    def next_step(self, result: ToolResult):

        if result.success:
            return None

        if result.tool == "run_python":

            if "SyntaxError" in result.error:
                return {
                    "tool": "read_file",
                    "filename": "main.py"
                }

        return None