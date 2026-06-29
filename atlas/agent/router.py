from atlas.agent.agent import AtlasAgent

agent = AtlasAgent()


def process_message(text: str) -> str:
    return agent.process(text)