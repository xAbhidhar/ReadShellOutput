# ReadShellOutput
 The project is about reading commands from a text file and processing various shell commands.
The input is a txt file containing valid and invalid commands. only valid commands are to be executed.

# Input
The input file contains two types of commands. Valid commands and invalid commands. The file will always have the invalid commands first and the valid commands after. Only the valid commands needs to be executed.

# Implementations

1. The commands must have a exact match which is case sensitive for the entire command string in the valid commands
2. All the commands which are uinvalid should be ignored.
3. The commands file for input is named as "commands.txt"
4. Each input command file is self validating. The commands in the valid section of one file does not affect what is valid in another file
5. It could be assumed that the commands file will fit into the memory

# Tools used
- Python
- Docker
- sql achemy

# STEPS

# DATABASE
The output of the command (if valid command) must be stored in the database. the datavse being used is sql alchemy.

# Result
the commands in valid command list is executed amd the details are stored in the database.
