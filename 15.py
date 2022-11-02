D = {
     "Value": 12345678980,
     "Hello": "World",
}
print(D)
D["World"] = "Hello"
print(D)
D.popitem()
A = D.get("Hello")
print(A)
for x,y in D.items():
    print(x,y)