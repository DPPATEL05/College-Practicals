s = input("Enter a string: ")
a=[]
b=[]
for i in s:
    if (i=='a') or (i=='e') or (i=='i') or  (i=='o') or (i=='u'):
        a.append(i)
    else:
        b.append(i)
T = tuple(a)
T1 =tuple(b)
print("Vowels in a given string: ",T)
print("Consonants in a given string: ",T1)
