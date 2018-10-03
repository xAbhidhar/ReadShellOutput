import json
import command_parser
import os
valid_commands = {}
list_of_dict = []
flag = 0
count_valid_command = 0
count_commands_to_be_executed = 0

with open('commands.txt', mode='r') as f:
    for command in  f:
        if command=='\n':
            flag = 1
            if count_valid_command%5!=0:
                with open("{}.json".format(str(count_valid_command)), 'w') as fp:
                    json.dump(valid_commands, fp)
                    list_of_dict.append("{}.json".format(str(count_valid_command)))
            continue
        command = command[0:-1]
        if flag == 0:
            valid_commands[command] = 1
            count_valid_command +=1
        else:
            #Check if the Command is present in the Valid Section and the Value of the command is = 1
            is_command_in_valid_commands = 0
            temp_dict = {}
            for json_file in list_of_dict:
                temp_dict = json.load(open(json_file))
                if command in temp_dict and temp_dict[command]==1:
                    with open(json_file,mode='w') as fp:
                        temp_dict[command] = 0
                        json.dump(temp_dict,fp)
                    # command_parser.process_command_output(command)
                    print(command)
                    continue

        if count_valid_command%5==0 and flag == 0:
            with open("{}.json".format(str(count_valid_command)), 'w') as fp:
                valid_commands.pop("[VALID_COMMANDS]", None)
                json.dump(valid_commands, fp)
                valid_commands={}
                list_of_dict.append("{}.json".format(str(count_valid_command)))
for json_file in list_of_dict:
    os.remove(json_file)

