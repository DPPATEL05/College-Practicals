a = ord('!')
b = ord('~')

for i in range(a, b+1):
    print("{} = {} = {}".format(chr(i), ord(chr(i)), hex(ord(chr(i)))))
