from atlas.tools.loader import load_tools
from atlas.tools.registry import get


class Executor:

    def __init__(self):

        load_tools()

    def run(self, tool_name, **kwargs):

        tool = get(tool_name)

        if tool is None:
            return f"Инструмент '{tool_name}' не найден."

        return tool.execute(**kwargs)