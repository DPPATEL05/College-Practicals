n = 5
for i in range(0,n+1):
    space = n - i
    for k in range(0, space):
        print(end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print()

for i in range(1,n+2):
    for j in range(1,i):
        print(j, end=" ")
    print()
