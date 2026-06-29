class ToolResult:

    def __init__(
        self,
        success: bool,
        tool: str,
        output: str = "",
        error: str = "",
    ):
        self.success = success
        self.tool = tool
        self.output = output
        self.error = error

    def __str__(self):
        if self.success:
            return self.output

        return self.error