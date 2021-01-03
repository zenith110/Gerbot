import os
from pathlib2 import Path
import re

"""
Utalizes the current state to determine if local or prod debugging is necessary
"""


def DebuggerSwitch(prod_mode: bool):
    file_data = []
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            file_directory = os.path.join("./cogs", filename)
            path = Path(file_directory)
            text = path.read_text()
            true_check = re.findall("prod_mode = True", text)
            false_check = re.findall("prod_mode = False", text)
            if true_check:
                text = text.replace("prod_mode = True", "prod_mode = " + str(prod_mode))
            elif false_check:
                text = text.replace(
                    "prod_mode = False", "prod_mode = " + str(prod_mode)
                )
            path.write_text(text)
