fib1=0
fib2=1

x=int(input("Enter a number"))
i=1
while i<=x:
    if i==1:
        print(0)
    elif i==2:
        print(1)
    else:
        fib=fib1+fib2
        print(fib)
        fib1=fib2
        fib2=fib
    i+=1
print("BYe")