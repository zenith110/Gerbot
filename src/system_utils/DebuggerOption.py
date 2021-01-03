import os

"""
Uses prod_mode flag to determines if enviroment is local or production
"""


def DebuggerOption(prod_mode):
    if prod_mode == True:
        from system_utils.ContainerLogger import ContainerLogger

        container_logger()
    else:
        from system_utils.LocalLogger import LocalLogger

        LocalLogger()
