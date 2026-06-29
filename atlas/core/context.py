class Context:

    def __init__(self, user_input: str):
        self.user_input = user_input

        self.plan = None

        self.results = []

        self.memory = {}

        self.finished = False