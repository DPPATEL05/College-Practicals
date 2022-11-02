l = []
a = int(input("Enter the number of elements you want to enter: "))
for i in range(0, a):
    n = int(input("Enter number {}: " .format(i+1)))
    l.append(n)
print("Initial List: ", l)
zeros, pos, neg = 0, 0, 0
for i in l:
    if i > 0:
        pos = pos+1
    elif i == 0:
        zeros = zeros+1
    else:
        neg = neg+1
print("Total zeros in list: ", zeros)
print("Total positive in list: ", pos)
print("Total negative in list: ", neg)
""""odd, even = 0, 0
for i in l:
    if i % 2 == 0:
        print(i," number is even")
        even = even+1
    else:
        print(i," number is odd")
        odd = odd+1
print("Total even numbers in list: ", even)
print("Total odd numbers in list: ",odd)

sum = sum(l)
print("Sum of list {} is: {}" .format(l, sum))
avg = sum/a
print("Average of list {} is: {}" .format(l, avg))"""