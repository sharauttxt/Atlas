from pathlib import Path


class ListFilesTool:

    def execute(self):

        workspace = Path.cwd() / "workspace"

        result = []

        for file in workspace.rglob("*"):

            if file.is_file():

                result.append(
                    str(file.relative_to(workspace))
                )

        return result