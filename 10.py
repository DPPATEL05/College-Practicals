for i in range(1, 10001):
    sums = 0
    for j in range(1, i):
        if i%j == 0:
            sums = sums+j
#            print(sums)
    if i == sums:
        print(i, "is a perfect positive integer")