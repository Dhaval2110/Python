# What is getattr ?

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)


# how to define switch case

# def switch(case):
# 	switcher={
# 	'Name':'Dhaval',
# 	'Class':'A1',
# 	'No':10}
# 	print(switcher.get(case))

# switch('Name')
