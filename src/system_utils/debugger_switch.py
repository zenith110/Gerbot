
import os
from pathlib2 import Path

"""
Utalizes the current state to determine if local or prod debugging is necessary
"""
def debugger_switch(prod_mode):
    file_data = []
    print(os.getcwd())
    command_builder = "./system_utils/command_builder.py"
    path = Path(command_builder)
    text = path.read_text()
    text = text.replace("prod_mode = True", "prod_mode = " + str(prod_mode))
    path.write_text(text)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            file_directory = os.path.join("./cogs", filename)
            path = Path(file_directory)
            text = path.read_text()
            text = text.replace("prod_mode = True", "prod_mode = " + str(prod_mode))
            path.write_text(text)
    
    
