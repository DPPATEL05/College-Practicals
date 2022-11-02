def fibonacci(a):
    n,n1=0,1
    if(a>1):
        for i in range(1,a):
            f=n+n1
            n=n1
            n1=f
            print(f)
    else:
       print("Enter value more than one")
a = int(input("Enter the value to print Fibonacci series: "))
fibonacci(a)