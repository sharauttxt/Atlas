import importlib
from pathlib import Path


def load_tools():

    tools_path = Path(__file__).parent

    for file in tools_path.glob("*.py"):

        if file.stem.startswith("_"):
            continue

        if file.stem in [
            "base",
            "registry",
            "loader",
            "__init__",
        ]:
            continue

        importlib.import_module(
            f"atlas.tools.{file.stem}"
        )