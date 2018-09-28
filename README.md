# ReadShellOutput
The project is about reading commands from a text file and processing various shell commands.
The input is a txt file containing valid and invalid commands. only valid commands are to be executed.

## Problem Statement
To build and make a deployable, containerized service that executes and processes valid shell command strings.

## Details
The service listens for POST requests at a specified endpoint containing a multi-part encoded file parameter. This file is parsed to determine the set of valid commands to be executed. The `commands.txt` file in this repository contains the commands and serves as an example to give a sense how the input file will be formatted. 

## Libraries Used

## Implementations

### Input
The input file contains two types of commands. Valid commands and invalid commands. The file will always have the invalid commands first and the valid commands after. Only the valid commands needs to be executed.

### Implementations Specifics
1. The commands must have a exact match which is case sensitive for the entire command string in the valid commands
2. All the commands which are uinvalid should be ignored.
3. The commands file for input is named as "commands.txt"
- For every valid command, you need to execute it and store the following meta-data:
  - actual command itself as a string
  - length of command string
  - time to complete (if the command takes > 1 minute to complete, mark a 0
    value which will represent a "long running or not finished" scenario.
  - stdout output from executing the command.
4. Each input command file is self validating. The commands in the valid section of one file does not affect what is valid in another file
5. It could be assumed that the commands file will fit into the memory

## Tools used
   - Python
   - Docker
   - sql achemy

## STEPS

   - Starts the docker container 
   - run the command for making containers 

## DATABASE
The output of the command (if valid command) must be stored in the database. the datavse being used is sql alchemy.

## Result
- The valid commands in command list is executed
- Execution details are stored in the database.
