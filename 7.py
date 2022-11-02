n = int(input("Enter how many number you want to enter"))
i = 0
sum = 0
while i<n:
    a = eval(input("Enter number"))
    sum = sum+a
    i=i+1
avg = sum/n
print("Average is: ", avg)