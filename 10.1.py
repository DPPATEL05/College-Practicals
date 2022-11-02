s = input("Enter the string: ")
flag = 0
s = s.lower()
r = "".join(reversed(s))
a = len(s)
for i in range(0,a):
    if(s[i]==r[i]):
        flag = 1
    else:
        flag=0
        break
if(flag==1):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")