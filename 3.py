a = eval(input("Enter  number1: "))
b = eval(input("Enter  number1: "))
c = eval(input("Enter  number1: "))
max = (a if (a>b and a>c)
       else(b if (b>c)
            else(c)))
print("Maximum number among {}, {} and {} is {}".format(a,b,c,max))