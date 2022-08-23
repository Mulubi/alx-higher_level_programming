# 0x00. Python - Hello, World

## About
This repository contains introductory projects for Python programming at first. The topics covered include:
- The Zen of Python.
- Using the Python Interpreter.
- Printing text and variables using print command.
- Using strings.
- Indexing and slicing in Python.
- Official Python coding style and how to check code with pycodestyle.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of files are to be tested using wc
### Shell Scripts
- Allowed editors: vi, vim, emacs
- All scripts will be tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (wc -l file should print 2)
- All files should end with a new line
- The first line of all files should be exactly #!/bin/bash
- All files must be executable
### C Scripts
- Allowed editors: vi, vim, emacs
- All files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All files should end with a new line
- Code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- Not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all functions are to be included in the header file called lists.h
- Don’t forget to push your header file
- All header files should be include guarded

## File Descriptions
### Mandatory
**[0-run](0-run)** - A Shell script that runs a Python script.

**[0-run.py](0-run.py)** - The Python file name will be saved in the environment variable $PYFILE

**[1-run_inline](1-run_inline)** - A Shell script that runs Python code.

**[1-run_inline.py](1-run_inline.py)** - The Python code will be saved in the environment variable $PYCODE

**[2-print.py](2-print.py)** - A Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line. The function print is used.

**[3-print_number.py](3-print_number.py)** - Print the integer stored in the variable number, followed by Battery street, followed by a new line. The output of the script should be the number, followed by Battery street, followed by a new line. Not allowed to cast the variable number into a string and the code must be 3 lines long. Have to use f-strings.

**[4-print_float.py](4-print_float.py)** - Print the float stored in the variable number with a precision of 2 digits. The output of the program should be: Float:, followed by the float with only 2 digits followed by a new line. Not allowed to cast number to string. Have to use f-strings.

**[5-print_string.py](5-print_string.py)** - Print 3 times a string stored in the variable str, followed by its first 9 characters. The output of the program should be: 3 times the value of str followed by a new line followed by the 9 first characters of str followed by a new line. Not allowed to use any loops or conditional statement. Program should be maximum 5 lines long.

**[6-concat.py](6-concat.py)** - Print Welcome to Holberton School! Not allowed to use any loops or conditional statements. Have to use the variables str1 and str2 in your new line of code. Program should be exactly 5 lines long.

**[7-edges.py](7-edges.py)** - Not allowed to use any loops or conditional statements. Program should be exactly 8 lines long. word_first_3 should contain the first 3 letters of the variable word. word_last_2 should contain the last 2 letters of the variable word. middle_word should contain the value of the variable word without the first and last letters.

**[8-concat_edges.py](8-concat_edges.py)** -  Print object-oriented programming with Python, followed by a new line. Not allowed to use any loops or conditional statements. Program should be exactly 5 lines long. Not allowed to create new variables. Not allowed to use string literals.

**[9-easter_egg.py](9-easter_egg.py)** - A Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.The script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py).

**[10-check_cycle.c](10-check_cycle.c)** - A function in C that checks if a singly linked list has a cycle in it. Requirements: Only these functions are allowed: write, printf, putchar, puts, malloc, free .

### Advanced
**[100-write.py](100-write.py)** - A Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line. Use the function write from the sys module. Not allowed to use print. Script should print to stderr. Script should exit with the status code 1.

**[101-compile](101-compile)** - A script that compiles a Python script file. The Python file name will be stored in the environment variable $PYFILE. The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc). 

**[102-magic_calculation.py](102-magic_calculation.py)** - Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
Tip: Python bytecode

### Others
**[lists.h](lists.h)** - Contains all the prototypes and the helper functions.
