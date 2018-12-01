'''
 What Are The Rules For Local And Global Variables In Python?

Answer :

In Python, variables that are only referenced inside a function are implicitly global. If a variable is assigned a new value anywhere within the function's body, it's assumed to be a local. If a variable is ever assigned a new value inside the function, the variable is implicitly local, and you need to explicitly declare it as 'global'.
Though a bit surprising at first, a moment's consideration explains this. On one hand, requiring global for assigned variables provides a bar against unintended side-effects. On the other hand, if global was required for all global references, you'd be using global all the time. You'd have to declare as global every reference to a builtin function or to a component of an imported module. This clutter would defeat the usefulness of the global declaration for identifying side-effects.

'''

# Example

#let a=10  as a global

a=10

def abc():
  print(a)
  a=a+2
  print(a)
 
 abc()
 
 # will throw an error : UnboundLocalError: local variable 'a' referenced before assignment
 # Now if we define global a inside fun in order to use in a function , it works fine i.e.
 
 
 a=10

def abc():
  global a                #Global varibale to be used in a function
  print(a)
  a=a+2
  print(a)
 
abc()
