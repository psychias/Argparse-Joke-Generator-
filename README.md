# Argparse-Joke-Generator
# Exercise 2


## Motivation

A command-line interface or command language interpreter (CLI), also known as command-line user interface, console user interface, and character user interface (CUI), is a means of interacting with a computer program where the user (or client) issues commands to the program in the form of successive lines of text (command lines).(Wiki)
Advantages of CLI: 
 

- Requires fewer resources
- Concise and powerful
- Expert-friendly
- Easier to automate via scripting

## Goal

The Goal for this project, was by reusing the Joke and JokeGenerator classes from the previous assignments  and create a command-line interface (CLI) using argparse.


## Summary

This python package can take an file as an input (otherwise the reddit_dadjokes.csv will be used as default ) and produces different arguments accordinly :

- A single joke will be printend with the information of the author, link to the joke, rating, and time specified as additional arguments over the command line by using the argument --print
- The jokes will be printed from the provided file (either from the user or by default) using the arguments --profanity_file [name of the file] 
- --output_file save_my_output.txt where the user should give the input and the output file of the joke
- The --split_sent argument prints the jokes from the provided file separated into sentences
- The --tokenize prints the jokes from the provided file separated into sentences and tokens

- Last but not least, by calling the argument --filter, the jokes from the provided file will be separated into sentences and tokens. 
  The user could provide a text file containing profanities otherwise the profinities text file will be used as default. 
  Additional, the user shoulf provide an output file to save the output of the --filter argument. If none output is provided, the sentece will be
  printed to standard output.

- For the user to be able to print the following arguments, it is necessary to use the argument --print before other arguments.
    For instance:
        - to print the jokes from the provided file separated into sentences -> the --print --split_sent are needed.



The user can , after having install the package, just type jg --print in his commant line and the joke will be printed.
This enables the user the possibility to run the script from anywhere.


For the test of this module, we were using a virtual enviroment in python.


## License

We choose the MIT license since we wanted to give users express permission to reuse our code for any purpose, sometimes even if code is part of proprietary software. 
As long as users include the original copy of the MIT license in their distribution, they can make any changes or modifications to the code to suit their own needs.

It is one of the most simple open source license agreements. The intent was for the text to be understandable by average users and to avoid extensive litigation




