# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:07:37 2022

@author: Dhaval
"""

# Global import 
import argparse

#------------------------------------------------------------------------------
# Name : argParsing
# Description : To check if arguments passed to command 
# Return Value : Arguments which are passed in command line
#------------------------------------------------------------------------------
def argParsing():
    sProg = 'pattern_find.py'
    sDesc = "argument parsing"
    oParser = argparse.ArgumentParser(prog=sProg,
                                      formatter_class=argparse.RawDescriptionHelpFormatter,
                                      description=sDesc,epilog = './python_parser.py --regex [pattern] --files [file]')
    oParser.add_argument('-r','--regex',dest="sPattern", required=True,
                         type=str, help="Pass the regex pattern")
    oParser.add_argument('-f','--filename',dest='sFile',required=True,
                         type=str, nargs='+',help="Pass the filename")
    oParser.add_argument('-u', '--underline',dest='underline',action='store_true',
                         help='underline')
    oParser.add_argument('-c', '--color', dest='color',action='store_true' ,
                         help='color')
    oParser.add_argument('-m', '--machine', action='store_true',
                         help='machine')
    args = oParser.parse_args()

    return args
    