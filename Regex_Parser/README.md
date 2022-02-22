# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:42:49 2022

@author: Dhaval
"""

The exercise:
Implement a Python script, that searches for lines matching regular expression -r (--regex) in file/s -f (--files).
Use STDIN if file/s option wasn’t provided.
Assume that input is ASCII, you don't need to deal with a different encoding.
If a line matches, print it. Please print the file name and the line number for every match.
The script accepts list optional parameters which are mutually exclusive:
-u ( --underscore ) which prints '^' under the matching text
-c ( --color ) which highlight matching text [1]
-m ( --machine ) which generate machine-readable output
                  format: file_name:no_line:start_pos:matched_text
Multiple matches on a single line are allowed, without overlapping.
The script should be compatible in line with
PEP8 coding guidelines. Please add proper documentation and error
handling.
Hint: It is recommended to use a module for parsing the command line
arguments and the "re" module for matching the pattern.
Try to use OOP in order to encapsulate differences between output
formats. Please put into comments what design pattern it follows.
[1] http://www.pixelbeat.org/


# FILES
1. argparser.py
--> to pass the command line arguments
2. main_method.py
--> A class method to find the pattern matching in file

# USAGE
Command : python main_method.py -r <regex_pattern> -f <file_name> [...optional arguments if any]
-------
Example : python main_method.py -r \d+ -f words.txt  -u  -c -m
Description : This command matches lines having digits

Or <---
If there is no file name passed then STDIN as an input
Ex : python main_method.py -r \w -f "DHAVAL" -u -c -m
