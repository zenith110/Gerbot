import os

"""
Uses prod_mode flag to determines if enviroment is local or production
"""


def debugger_option(prod_mode):
    if prod_mode == True:
        from system_utils.container_logger import container_logger

        container_logger()
    else:
        from system_utils.local_logger import local_logger

        local_logger()
