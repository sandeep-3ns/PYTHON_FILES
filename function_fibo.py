def fibonacci(n):
    fib1,fib2=0,1
    print(fib1,fib2,end=' ')
    for i in range(n-2):
        fib=fib1+fib2
        print(fib,end='  ')
        fib1,fib2=fib2,fib



fibonacci(10)