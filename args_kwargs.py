'''
Q:What Does The *Args Do In Python?
Ans:We use *args as a parameter in the function header. It gives us the ability to pass N (variable) number of arguments.

Please note that this type of argument syntax doesn’t allow passing a named argument to the function.

Example of using the *args:
'''
# Python code to demonstrate 
# *args for dynamic arguments 
def fn(*argList):  
    for argx in argList:  
        print (argx) 
    
fn('I', 'am', 'Learning', 'Python')

'''
Q: What Does The **Kwargs Do In Python?
We can also use the **kwargs syntax in a Python function declaration. It let us pass N (variable) number of arguments which can be named or keyworded.

Example of using the **kwargs:
'''
# Python code to demonstrate 
# **kwargs for dynamic + named arguments 
def fn(**kwargs):  
    for emp, age in kwargs.items(): 
        print ("%s's age is %s." %(emp, age)) 
    
fn(John=25, Kalley=22, Tom=32)
