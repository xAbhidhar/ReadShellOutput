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

def process_command_output(bashCommand):
    # TODO: execute the command and put its data in the db
    try:
        stime = time.time()
        output = subprocess.check_output(['bash', '-c', bashCommand], timeout=5)
        ftime = time.time()
        push_database(bashCommand,len(bashCommand),ftime - stime,output)
    except subprocess.TimeoutExpired:
        push_database(bashCommand,len(bashCommand),0,"long running or not finished")
    except subprocess.CalledProcessError:
        return bashCommand
    return True

def push_database(comm, length, dur, out):
    # print("This result will be cached in the DataBase")
    # print("Command: "+str(comm))
    # print("Lenght of Command:" + str(length))
    # print("Duration of Command Execution: " + str(dur))
    # print("Output of each Command: "+str(out))
    # print("*********************************************************************")
    row = Command(command_string=comm, length=length, duration=dur, output=out)
    session.add(row)
    session.commit()
    session.close()

#Function for printing the databse
def db_print():
    conn = engine.connect()
    select_st = select([Command])
    res = conn.execute(select_st)
    for _row in res: print (_row)
