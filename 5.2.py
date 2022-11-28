a=[]
print("Enter 10 numbers: ")
for i in range(0,10):
    a.append(int(input()))

for i in a:
    for j in a:
        print(i,j)
