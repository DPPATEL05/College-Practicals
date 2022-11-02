def n_list(s):
    print("List before deleting duplicate values: ",s)
    a = set(s)
    s = list(a)
    return s

L = ["A", 1, "B", 1, "C", 1]
a = n_list(L)
print(a)

