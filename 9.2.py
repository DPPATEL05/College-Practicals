import random
scpg = int(input("""
Enter 0 for scissor
Enter 1 for rock
Enter 2 for paper"""))
n = random.randint(0,2)
if(scpg>2):
    print("Enter valid option")
elif(n==scpg):
    print("Draw")
elif(n==2 and scpg==0)or(n==0 and scpg==1)or(n==1 and scpg==2):
    print("User Wins")
else:
    print("Computer Wins")