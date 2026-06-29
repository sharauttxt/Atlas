from atlas.reasoner.reasoner import Reasoner
from atlas.ai.manager import ask
from atlas.executor.executor import Executor
from atlas.planner.planner import Planner
from atlas.tools.manager import ToolManager


class AtlasAgent:

    def __init__(self):

        self.planner = Planner()
        self.tools = ToolManager()
        self.executor = Executor(self.tools)
        self.reasoner = Reasoner()

    def process(self, text: str):

        plan = self.planner.plan(text)

        # Если Planner решил просто ответить
        if plan.get("tool") == "chat":
            return ask(text)

        results = self.executor.execute(plan)

        if results is None:
            return ask(text)

        answer = []

        for result in results:
            answer.append(str(result))

        return "\n\n".join(answer)