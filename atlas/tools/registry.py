TOOLS = {}


def register(tool):
    TOOLS[tool.name] = tool


def get(name):
    return TOOLS.get(name)


def all_tools():
    return TOOLS