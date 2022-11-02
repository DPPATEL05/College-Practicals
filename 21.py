def GCD (n, m):
    if m == 0:
        return n
    return GCD(m, n%m)

a= GCD(36,60)
print(a)