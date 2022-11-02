s = "PYthon"
sum=0
a = len(s)
s = s.lower()
for i in range(0,a):
    for j in range(1,27):
            print(chr(96+j))
            sum=j+sum
print(sum)