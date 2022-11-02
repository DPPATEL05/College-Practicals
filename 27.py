import cmath
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))
d = (b*b) - (4*a*c)
r = (-b + cmath.sqrt(d))/(2*a)
r1 = (-b - cmath.sqrt(d))/(2*a)
print("Real roots of a given equation are {} and {}".format(r,r1))