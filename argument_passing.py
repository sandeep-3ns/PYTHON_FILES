def modify(x):
    print(id(x))
    x[2]=0
    print(id(x))
    print(x)

lst=[1,20,30,40]
print(id(lst))
modify(lst)
print(lst)
