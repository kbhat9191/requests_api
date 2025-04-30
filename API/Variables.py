import keyword
a = 11
b = 28

print(a, "->", type(a))
# print(len(a))
# TypeError: object of type 'int' has no len()

c = 'welcome'
print(c, "->", type(c))
print(len(c))

if a > b:
    print("a is greater than b",(a > b))
elif a < b:
    print("A is smaller than b", (a < b))
elif a == b:
    print("a is equal to b", (a == b))
else:
    print("End of if loop")
print("End of program")
"""
comments
this is multiline
comments
"""

# single line comment

'''
comments
this is multiline
comments
'''

name = input("Enter name: ")
empid = input("Enter empid: ")
print("Welcome", name, empid)

print(keyword.kwlist)