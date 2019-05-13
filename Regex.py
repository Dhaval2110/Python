# a="Dhaval@1234$& Mehta\n"

# import re
# NameAge= "Juan is 30 and Degea is 25 Rashford is 19 and Lingard is 21"
# Names=re.findall(r'[A-Z][a-z]*',NameAge)
# Ages=re.findall(r'\d{1,9}',NameAge)

# print Names,Ages

# Dict=dict(zip(Names,Ages))
# print Dict

'''
Let match a valid command
'''
import re
#temp="AT+asx=9865"
temp="AT+asx^9865=dw?"
if re.match(r'AT+(\W.*)(=|\^)(\d.*)',temp):       # It always gives true or false
	print("True")
else:
	print("False")
 

