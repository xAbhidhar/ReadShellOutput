# commands = {
#   "COMMAND_LIST": [
#     "ls",
# "pwd",
# "echo \"hello there\"",
# "grep \"ls\" commands.txt",
# "grep \"pwd\" commands.txt",
# "grep \"pwd\" commands.txt",
# "grep \"tacos\" commands.txt",
# "this isn't valid",
# "echo \"hello there\"",
# "while true; do echo 'Ctrl c to kill'; sleep 1; done",
# "grep \"pwd\" commands.txt",
# "this also isn't valid",
# "while true; do echo 'Ctrl c to kill again'; sleep 1; done",
# "grep \"pwd\" commands.txt",
# "grep \"pwd\" commands.txt",
# "ps",
# "echo \":(){ :|: & };:\" > /tmp/mymaliciousFile; chmod 777 /tmp/mymaliciousFile; ./tmp/mymaliciousFile"
#
#     ],
#   "VALID_COMMANDS": [
#     "ls",
#     "echo \"hello there\"",
#     "pwd",
#     "grep \"pwd\" commands.txt",
#     "grep \"ls\" commands.txt",
#     "while true; do echo 'Ctrl c to kill'; sleep 1; done",
#     "cat",
#     "ps"
#   ]
# }
#
# for key,value in commands.items():
#     for i in value:
#         print(i)


# d = {"hey":1}
# if "HEy" in d:
#     print("hey is there ")


# from multiprocessing import Process, Queue
# queue = Queue()
# queue.put("hey")
# queue.put("hi")
# print(queue.get())
# queue.empty()
# print(queue.empty())
# print(queue.get())
# queue.empty()
# print(queue.empty())
#
# print(queue.empty())
#


# bashCommand = "while true; do echo 'Ctrl c to kill'; sleep 1; done"
# bashCommand = "while true; do echo 'Ctrl c to kill'; sleep 1; done"
import time

# bashCommand = "while true; do echo 'Ctrl c to kill'; sleep 1; done"
# bashCommand = "grep \"pwd\" commands.txt"
# import subprocess
#
# # output = subprocess.check_output(['bash','-c', bashCommand],timeout=5)
# # print(output)
# try:
#     stime = time.time()
#     output = subprocess.check_output(['bash','-c', bashCommand],timeout=5)
#     ftime = time.time()
#     print("Execution time:" + str(ftime-stime))
#     print(output)
# except subprocess.TimeoutExpired:
#     print("The Command timed out")
# except subprocess.CalledProcessError:
#     print("The Command is Invalid")






# subprocess.Popen("while true; do echo 'Ctrl c to kill'; sleep 1; done")


# from subprocess import call
# call(["ls","-l"])
#


# from sultan.api import Sultan
# s = Sultan()
# print(s.sudo("yum install -y tree").run())
# import subprocess
# try:
#
#     # print(subprocess.Popen("ls"))
#     subprocess.Popen("grep \"tacos\"  commands.txt")
# except:
#     print("Error while readinf file")




#Checking the AST generator BashLex

import bashlex
# parts = (list(bashlex.split("echo \":(){ :|: & };:\" > /tmp/mymaliciousFile; chmod 777 /tmp/mymaliciousFile; ./tmp/mymaliciousFile")))
# parts = bashlex.parse("ls /tmp/foo")
# parts = bashlex.parse("rm -rf a* > foo")
from bashlex.ast import nodevisitor
# bashCommand = "echo \":(){ :|: & };:\" > /tmp/mymaliciousFile; chmod 777 /tmp/mymaliciousFile; ./tmp/mymaliciousFile"
# bashCommand = "echo \"hello\" > foo"
# # bashCommand = "rm - rm"
# parts = bashlex.parse(bashCommand)
# print(parts[0].dump())
# print(type(parts[0].parts[0]))

# i = 0
# while True:
#             try:
#                if (parts[0].parts[i].word) == 'rm' or (parts[0].parts[i].word) == 'unlinlk':
#                    print(bashCommand)
#
#                i = i + 1
#             except IndexError:
#                 break




# print(type(parts))
# print(parts[0])
# print(parts)
# import json
# print(json.load(open('commands.json',mode='r')))

# Finding Malacious commands
#
import bashlex
# to check if a command is trying to update a temp directory.
parts = bashlex.parse('while true; do echo \'Ctrl c to kill\'; sleep 1; done')
# parts = bashlex.parse('ls > /tmp/foo')

# print(parts[0].dump())
# print(parts[0].parts[2].type)
# # print(parts[0].parts[2].word)
# print(parts[0].parts[2].output.word)

print(parts[0].dump())
print(parts[0].list[0])
# s = '/tmp'
# if s in '/tmp/foo':
#     print("hey")