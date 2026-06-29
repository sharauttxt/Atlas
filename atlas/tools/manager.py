from atlas.tools.read_file import ReadFileTool


class ToolManager:
    def __init__(self):
        self.read_file = ReadFileTool()

    def execute(self, tool_name: str, **kwargs):
        if tool_name == "read_file":
            return self.read_file.execute(kwargs["filename"])

        return f"Неизвестный инструмент: {tool_name}"