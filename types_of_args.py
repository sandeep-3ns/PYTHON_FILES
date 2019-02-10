def person(name,age):
    print(name,age)

person('dhoni',37)
#  the problem comes when u dont no the order of the argumengts
# we are to pass
"""person(age,name) if we pass like this and inside a function if we are doing
operation on age
it gives a error because the operation will be done on other argument"""


"""example of default parameters"""
def display(name,age=22):
    print("Name ",name,"Age ",age )
display('dhoni',37)
display('sandeep')

#example on variable length parameters

def add(a,*b):
    print(type(b))
    c=a
    for i in b:
        c+=i
    print(c)

add(10,200,1,1,1,1,1)