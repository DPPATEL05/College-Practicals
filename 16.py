import random


def shuffl(s):
    print(s)
    print("After shuffling: ")
    random.shuffle(s)
    print(s)


L = ["A", 1, "B", 2, "C", 3]
shuffl(L)
