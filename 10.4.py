s = input("Enter the first string: ")
r = input("Enter the second string: ")
flag=0
a = len(s)
b=len(r)
if(a==b):
    for i in range(0,a):
        for j in range(0,b):
            if(s[i]==r[j]):
                flag=1
        if(flag!=1):
            flag=0
            break
else:
    flag=0
if(flag==1):
    print("Given string is anagrams")
else:
    print("Given string is not anagrams")