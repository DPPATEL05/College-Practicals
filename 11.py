l = [1, 2, 3, 4, 5]
print("Initial list: ", l)
print("Element at first position: ", l[1])
print("Element at last position:", l[-1])
l.append(6)
print("List after appending:", l)
l1 = [7, 8]
l.append(l1)
print("List after inserting anther list:", l)
l.insert(1,'Hello')
print("List after inserting lement at first position: ", l)
l2 = [10, 11]
l.insert(6, l2)
print("List after inserting another list at sixth position: ", l)
l.remove(4)
print("List after removing an element at position 4: ", l)
a=l.pop(3)
print("List after rmeoving an element using pop method at position 4 and value removed is stored in a:", a)
l.reverse()
print("List after reversing the list: ", l)
