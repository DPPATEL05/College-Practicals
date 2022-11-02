rows = 5
col = 5
n = 1
for n in range(1, rows+1):
    for j in range(1, n+1):
        print(j, end=" ")
        j = j+1
    print("\r")
