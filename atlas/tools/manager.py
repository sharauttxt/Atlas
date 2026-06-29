import atlas.tools

from atlas.tools.registry import get


class ToolManager:

    def execute(self, tool_name: str, **kwargs):

        tool = get(tool_name)

        if tool is None:
            return f"Неизвестный инструмент: {tool_name}"

        return tool.execute(**kwargs)