"""
Handles the work of validating and processing command input.
"""
import subprocess

import time

from sqlalchemy import select

from db import *
from base import *
from base import Command

def get_valid_commands(fileDict):
    # TODO: efficiently evaluate commands from filename passed
    valid_commands = {}
    valid_command_to_be_executed = {}
    for i in fileDict:
        if i =='VALID_COMMANDS':
            for command in fileDict[i]:
                if command not in valid_commands:
                    valid_commands[command] =1
        else:
            for command in fileDict[i]:
                if command  in valid_commands and command not in valid_command_to_be_executed:
                    valid_command_to_be_executed[command] = 1
                    #Pass the command to process Commands method.
                    print("Valid Command send for execution: " + command)
                    res = process_command_output(command)
                    if res !=True:
                        valid_commands.pop(res)
    db_print()
