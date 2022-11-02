per = eval(input("Enter your percentage: "))
def switch(per):
    if per >= 90:
        return "Grade: A"
        exit()
    elif per >= 80:
        return "Grade: B"
        exit()
    elif per >= 70:
        return "Grade: C"
        exit()
    elif per >= 60:
        return "Grade: D"
        exit()
    elif per >= 50:
        return "Grade: E"
        exit()
    else:
        return "Grade: F"
        exit()

print(switch(per))
