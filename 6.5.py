import  random
arr=[]
count,h1,counts=0,0,0
count1,h2,counted=0,0,0
rows, cols=4,4
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(random.randint(0,1))
    arr.append(col)
for rows in range(0,4):
    for cols in range(0,4):
        print(arr[rows][cols], end=" ")
    print()
for rows in range(0,4):
    count=0
    counts=0
    for cols in range(0,4):
        if(arr[rows][cols]==1):
            count = count + 1
        if (arr[cols][rows] == 1):
            counts = counts + 1
    if (counts >= counted):
        counted = counts
        h2 = rows + 1
    if(count>=count1):
        count1=count
        h1 = rows+1


print('Maximum numer of 1 is in row: ',h1)
print('Maximum number of 1 is in column: ',h2)
