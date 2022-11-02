weight = eval(input("Enter your weight in kg"))
height = eval(input("Enter your height in cm"))
h = height*0.01
print("Height in meter", h)
BMI = weight/(h*h)
print("Your BMI is: ", BMI)
if BMI < 19:
    print("You arte underweight")
elif BMI > 25:
    print("You are overweight")
else:
    print("You are healthy")