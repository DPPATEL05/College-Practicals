year = int(input("Enter a year"))
if year%4==0:
    print("Ït is a leap year")
elif year%400==0:
    print("It is a leap year")
else:
    print("It is a non-leap year")