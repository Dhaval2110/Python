# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 19:04:21 2022

@author: Dhaval
"""
# Write a program to conver numbers written on cheques in words.
# The number should not be greater than 7 digits

def convertToDigit(num, suffix):
#------------------------------------------------------------------------------
# Name : ConvertToDigit
# Description :Function to convert a single-digit or two-digit number into words
# Input : A number and suffix
#------------------------------------------------------------------------------
    if num == 0:                                                               # if number is zero
        return EMPTY  
    if num > 19:                                                               # split number if it is more than 19
        return Y[num // 10] + X[num % 10] + suffix
    else:
        return X[num] + suffix
 
 

def CheckBook_WordsPrint(n):
#------------------------------------------------------------------------------
# Name : CheckBook_WordsPrint
# Description : To print the digits in words upto 7 digits
# Input : A number as an integer
# Output : Result value in words
#_----------------------------------------------------------------------------- 
    lenth_number = len(str(n))                                                 # Find length of number
    print(lenth_number)
    try :
        if not lenth_number >8:                                                # If number is greater than 7 digits then raise exception
            result = convertToDigit(((n // 100000) % 100), 'Lakh, ')           # add digits at hundred thousand and one million place
            result += convertToDigit(((n // 1000) % 100), 'Thousand, ')        # add digits at thousand and tens thousand place
            result += convertToDigit(((n // 100) % 10), 'Hundred ')            # add digit at hundred place
            if n > 100 and n % 100:
                result += 'and '
            result += convertToDigit((n % 100), '')                            # add digits at ones and tens place
            return result.strip().rstrip(',').replace(', and', ' and')
        else:
            raise ValueError("Out of range!!")    
    except ValueError as err:
        print("Numbers are greater than 7 digits. {}".format(err))
     

#------------------------------------------------------------------------------
# Main 
#------------------------------------------------------------------------------
if __name__ == '__main__':
    EMPTY = ''
 
    X = [EMPTY, 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',  # 1-19 digits in words 
        'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
        'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
 
    Y = [EMPTY, EMPTY, 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ',               # twenty onwards in words 
        'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
 
    print(CheckBook_WordsPrint(99))                                            # Valid case 1 
    print(CheckBook_WordsPrint(1000))                                          # Valid case 2 
    print(CheckBook_WordsPrint(1463236))                                       # Valid case 3 
    print(CheckBook_WordsPrint(997751076))                                     # Invalid case 1
    print(CheckBook_WordsPrint(2147483647))                                    # Invalid case 2