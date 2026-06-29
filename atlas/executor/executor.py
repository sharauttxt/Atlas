class Executor:

    def __init__(self, tools):
        self.tools = tools

    def execute(self, plan):

        results = []

        # Старый формат
        if "tool" in plan:

            tool = plan["tool"]

            if tool == "chat":
                return None

            result = self.tools.execute(
                tool,
                **{
                    k: v
                    for k, v in plan.items()
                    if k != "tool"
                }
            )

            results.append(result)

            return results

        # Новый формат
        for step in plan["steps"]:

            tool = step["tool"]

            if tool == "chat":
                continue

            result = self.tools.execute(
                tool,
                **{
                    k: v
                    for k, v in step.items()
                    if k != "tool"
                }
            )

            results.append(result)

            # Если инструмент завершился ошибкой —
            # прекращаем выполнение плана.
            if not result.success:
                break

        return results