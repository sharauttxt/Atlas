from atlas.ai.manager import ask
from atlas.planner.planner import Planner
from atlas.tools.manager import ToolManager


class AtlasAgent:

    def __init__(self):

        self.planner = Planner()
        self.tools = ToolManager()

    def process(self, text: str):

        plan = self.planner.plan(text)

        if plan["tool"] == "chat":
            return ask(text)

        return self.tools.execute(
            plan["tool"],
            **{
                k: v
                for k, v in plan.items()
                if k != "tool"
            }
        )