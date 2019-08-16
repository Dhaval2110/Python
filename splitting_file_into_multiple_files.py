'''
Prerequisite : 
https://pypi.org/project/filesplit/

PS : Applicable for converting bat file as well :) 
'''


from fsplit.filesplit import FileSplit
fs = FileSplit(file=r"C:\Users\DHAVAL\Desktop\Old_resumes\really_big_file.txt", splitsize=500, output_dir=r"C:\Users\DHAVAL\Desktop\Old_resumes")
fs.split()
