import math
global l
l = []

def mean(a):
    c=a
    b = 0
    sum = 0
    for i in range (0,a):
        b = int(input("Ënter number {}: ".format(i+1)))
        sum = sum +b
        l.append(b)
    global avg
    avg = sum/c
    print(avg)
def deviation():
    dev = 0
    d = len(l)-1
    print(avg)
    t = tuple(l)
    for i in l:
        print(i)
        dev += ((i-avg)*(i-avg))
    de = dev/d
    deviation = math.sqrt(de)
    print(dev)
    print(de)
    print(deviation)
mean(4)
deviation()