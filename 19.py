import math

def prime (n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("Given number is not a prime number")
            else:
                print("Given number is a prime number")

prime (2)