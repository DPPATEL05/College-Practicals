import math
angle, height = map(eval, input("Ënter angle and height: ").split())
rad = math.radians(angle)
ang = math.cos(rad)
length= height/ang
print("Length of thge ladder required is: ",length)