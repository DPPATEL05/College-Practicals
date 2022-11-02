s="12203AB3"
appears = 0
for i in range(0,10):

   appears = 0
   #print(i)
   for j in s:
        if(str(i) == j):
            appears = appears + 1
   if(appears!=0):
       print("Digit {} appears {} times: ".format(i, appears))