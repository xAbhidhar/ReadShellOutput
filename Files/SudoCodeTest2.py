# # import argparse
# # from argparse import RawTextHelpFormatter
# #
# # from bashlex import parser, ast
# #
# #
# # class nodevisitor(ast.nodevisitor):
# #     def __init__(self, positions):
# #         self.positions = positions
# #
# #     def visitcommandsubstitution(self, n, command):
# #         # log the start and end positions of this command substitution
# #         self.positions.append(n.pos)
# #
# #         # do not recurse into child nodes
# #         return False
# #
# #
# # desc = '''replace all occurrences of $() and `` with the string given in -s
# #   $ commandsubstitution-remover.py -s nope -c 'foo $(bar)'
# #   foo nope
# # within words:
# #   $ commandsubstitution-remover.py -c '"foo $(bar) baz"'
# #   "foo XXX baz"
# # but not within single quotes, since they cancel special meaning:
# #   $ commandsubstitution-remover.py -c "foo '"'$(bar)'"'"
# #   foo '$(bar)'
# # (this a simple script to demonstrate how to traverse the ast produced
# # by bashlex)
# # '''
# #
# # if __name__ == '__main__':
# #     argparser = argparse.ArgumentParser(description=desc,
# #                                         formatter_class=RawTextHelpFormatter)
# #     # argparser.add_argument('-s', dest='replacement', metavar='S', default='XXX',
# #     #                        help='replace occurrences with S (default: XXX)')
# #     #
# #     # group = argparser.add_mutually_exclusive_group()
# #     # group.add_argument('-c', dest='expression',help='string to parse')
# #
# #     # args = argparser.parse_args()
# #     # s = "echo \"hello\" /tmp/foo"
# #     #
# #     # trees = parser.parse(s)
# #     # positions = []
# #     # for tree in trees:
# #     #     visitor = nodevisitor(positions)
# #     #     visitor.visit(tree)
# #     #
# #     # # do replacements from the end so the indicies will be correct
# #     # positions.reverse()
# #     # postprocessed = list(s)
# #     # for start, end in positions:
# #     #     # replace the portion of the input where the substitution occurred
# #     #     # with the replacement string
# #     #     postprocessed[start:end] = args.replacement
# #     # print(''.join(postprocessed))
# #     # print()
# #
# # # import ijson
# # #
# # # filename = "commands.json"
# # # with open(filename, 'r') as f:
# # #     objects = ijson.items(f, 'VALID_COMMANDS')
# # #     columns = list(objects)
# # # print(columns)
# # #
# #
# #
#
# # Code to read Text File and write into Json File.
# import command_parser
#
# valid_commands = {}
# valid_command_to_be_executed = {}
# flag = 0
# count_valid_command = 0
# count_commands_to_be_executed = 0
#
# with open('commands.txt', mode='r') as f:
#     for command in  f:
#         if command=='\n':
#             flag = 1
#             del valid_commands['[VALID_COMMANDS]']
#             count_valid_command = count_valid_command-1
#
#         if flag == 0:
#           if command not in valid_commands:
#                 valid_commands[command.replace('\n','')] = 1
#                 count_valid_command +=1
#         else:
#             if command in valid_commands and command not in valid_command_to_be_executed:
#                 valid_command_to_be_executed[command] = 1
#                 # Pass the command to process Commands method.
#                 print("Valid Command send for execution: " + command)
#                 res = command_parser.process_command_output(command)
#                 count_commands_to_be_executed +=1
#                 if res != True:
#                     valid_commands.pop(res)
#                     count_valid_command -=1
#                     del valid_command_to_be_executed[res]
#                     count_commands_to_be_executed-=1
#
#

# command = '[Valid_Commands]\n'
# print(command[0:-1])


# Checking the Continue VS Break.
# a = [1,2,3,4,5]
#
# for i in a:
#     if i == 3:
#         continue
          #break
#     print(i)

# Loading each json file into memory.

# import json
# data = json.load(open('5.json'))
# print(data)
# if 'pwd1' in data:
#     print('hey')

# Cleaning up the file:
# import os
# os.remove('5.json')


#Checking Try -catch:
# import bashlex
# import time
# import subprocess
#
# bashCommand = "while true; do echo \'Ctrl c to kill\'; sleep 1; done"
# parts = bashlex.parse(bashCommand)
# i = 0
# print("*********************************************")
# print(bashCommand)
# print("hey I am Here")
# check_flag = 1
# while check_flag == 1 and i<len(bashCommand):
#     print(i)
#     try:
#         try:
#             if (parts[0].parts[i].word) == 'rm' or (parts[0].parts[i].word) == 'unlink':
#                 break
#         except AttributeError:
#             pass
#         try:
#             if parts[0].parts[i].type == '>' and '/tmp' in parts[0].parts[i].output.word:
#                 print("Caught you Command")
#                 break
#         except AttributeError:
#             pass
#         i = i + 1
#     except IndexError:
#         print("Index Error")
#         check_flag = 0
#
#
# stime = time.time()
# try:
#     output = subprocess.check_output(['bash', '-c', bashCommand], timeout=.01)
#     ftime = time.time()
#     print("hey I am also Here")
#     print(bashCommand,len(bashCommand),0,output)
#     # push_database(bashCommand, len(bashCommand), int(ftime - stime), output)
# except subprocess.TimeoutExpired:
#     print(bashCommand,len(bashCommand),0,"longrunning")
#     # push_database(bashCommand, len(bashCommand), 0, "long running or not finished")
# except subprocess.CalledProcessError:
#     pass