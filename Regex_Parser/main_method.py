
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 00:10:40 2022

@author: Dhaval
"""

# global imports
import os
import re
import logging
import warnings

#local imports
from argparser import argParsing


# global/local variables
l=[]


#==============================================================================
# main class to perform patternmatching 
#==============================================================================
class PatternMatch():     
    #--------------------------------------------------------------------------
    # Name : constructor method 
    # Inputs : None
    # Description : Argparse return value , logging module initilization 
    #               and color code definition is defined in this consturctor
    # Output : None 
    #--------------------------------------------------------------------------                                                     
    def __init__(self):
        self.sVal = argParsing()                                               # calling method from pattern_find.py to fetch the cli inputs
        logging.basicConfig(filename='output.log', level=logging.DEBUG,        # Initializing logging file to save the output logs printed on console
                            format='%(message)s',filemode='w')
        
        self.CYAN = '\033[96m'                                                 # Color code for CYAN
        self.END = '\033[0m'                                                   # Color code for END  
     
    #--------------------------------------------------------------------------
    # Name:  argsaves method
    # Input : None
    # Description : The class method to read the file from commandline, process
    #               file line by line and match the pattern passed in command 
    #               line or match pattern to command line string
    #               print them in differnent formats based on
    #               optional parameters which are mutually exclusive.
    #               Logging console output to log file 'output.txt'
    # Output : Output.txt file and console output 
    #--------------------------------------------------------------------------
    def argSaves(self):     
        try:                                         
            if self.sVal.sFile:                                                # If file is passed as an argument 
                for files in self.sVal.sFile:                                  # Iterate for multiple files if passed
                    #----------------------------------------------------------
                    # Case 1 : If file is not passed as command line STDIN as 
                    #          input
                    #----------------------------------------------------------
                    if not os.path.exists(files):                              # Check if file is valid path or not
                        warnings.warn("File is not passed???")
                        match = re.search(self.sVal.sPattern,files)            #Check if regex pattern is matches with line
                        if match != None: 
                            if self.sVal.underline:                            #If underline is passed to command line print "^" to line on termina
                                print("{} matches in line {}"
                                      .format(match.group(0),files))
                                print("             " ,"^" * len(files) )
                            if self.sVal.color:                                #  Print color on console output when color argument is passed to a file
                                print("{} matches in line {}"
                                      .format(match.group(0),files) + self.END)
                            if self.sVal.machine:                              # print a machine readable format matched string to pattern as it does not have lines 
                                print("{}:{}".format((files),match.group(0)), 
                                      end="")
                            else:
                                print("{} matches in line {}"
                                      .format(match.group(0),files))

                    #----------------------------------------------------------
                    # Case 2: If files are passed as command line , filenames   
                    #         are as inputs
                    #----------------------------------------------------------
                    else:
                        with open(files,'r') as fd:                            # Open a file one by one to read
                            l = fd.readlines()                                 # Save the content lines of files into a list
                        
                        for i in range(0,len(l)) :                             # Iterate over list elements
                            match = re.search(self.sVal.sPattern,l[i])         # Check if regex pattern is matches with line
                            if match != None:                                  # In order to print the lines with matching pattern , ignore if no patten match
                                if self.sVal.underline:                        # If underline is passed to command line print "^" to line on terminal as well as in log file
                                    print("{} matches at line {} in file {}"
                                          .format(match.group(0),i+1,files))
                                    print("             " ,"^" * len(l[i]) )
                                    
                                    logging.info("{} matches at line {} in"
                                                 " file {}"
                                                 .format(match.group(0),
                                                         i+1,files))
                                    logging.info("             ^" )
                                    
                                if self.sVal.color:                            # Print color on console output when color argument is passed to a file
                                   print("{} matches at line {} in file {}"
                                         .format(match.group(0),i+1,files) + 
                                         self.CYAN + l[i] + self.END)
                                   
                                   logging.info("{} matches at line {} "
                                                " in file {}"
                                                .format(match.group(0),
                                                        i+1,files) +  
                                                self.CYAN + l[i] + self.END)
                               
                                if self.sVal.machine:                          # which generate machine-readable output , format: file_name:no_line:start_pos:matched_text
                                    print("{}:{}:{}".format(files, i+1, 
                                                            l[i]), end="")
                                else:                                          # if in case no optional arguments are passed
                                    print("{} matches at line {} in file "
                                          "{}".format(match.group(0),i+1,
                                                      files))
                                    logging.info("{} matches at line {} in "
                                                 "file {}"
                                                 .format(match.group(0),i+1,
                                                         files))
                                    
                                    
        except Exception :                                                     # Ignore case if file does not exists but use STDIN as input of -f
            pass
  

#------------------------------------------------------------------------------
# main function
#------------------------------------------------------------------------------
if __name__ == '__main__':
    c=PatternMatch()
    c.argSaves()