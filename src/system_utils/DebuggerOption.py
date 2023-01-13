import os

"""
Uses prod_mode flag to determines if enviroment is local or production
"""


def DebuggerOption(prod_mode: bool, webhook_url: str):
    if prod_mode == True:
        from system_utils.ContainerLogger import ContainerLogger

        ContainerLogger(webhook_url)
    else:
        from system_utils.LocalLogger import LocalLogger

        LocalLogger()
