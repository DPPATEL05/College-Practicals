import  random
arr=[]
count,h1,counts=0,0,0
count1,h2,counted=0,0,0
rows, cols=4,4
for rows in range(0,4):
    col = []
    for cols in range(0,4):
        col.append(random.randint(0,1))
    arr.append(col)
for rows in range(0,4):
    for cols in range(0,4):
        print(arr[rows][cols], end=" ")
    print()
for rows in range(0,4):
    count=0
    for cols in range(0,4):
        if(arr[rows][cols]==1):
            count = count + 1
    if(count>=count1):
        count1=count
        h1 = rows+1

for rows in range(0,4):
    counts=0
    for cols in range(0,4):
        if(arr[cols][rows]==1):
            counts = counts + 1
            print("Counts: ",counts)

    if(counts>=counted):
        print(cols)
        counted=counts
        h2 = rows+1


print('h1',h1)
print('h2',h2)
