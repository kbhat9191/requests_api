l1 = [1, 2.3, 'apple', "orange", True, [0, 2, 4, 6]]
print(l1, "\n", type(l1))
print(type(l1[5]))
print(l1[5])
print(l1[5][1])

l2 = [[0, 1, 2, 3], [4, 6, 7, 8], [9, 10, 11, 12]]
print(l2)
print(type(l2))
print(l2[2][2])
l2[1][0] = 33
print(l2)

# adding element to end of list
l3 = [10, 20, 30]
l3.append(22)
l3.append(44)
print(l3)

# adding element to the list on specific index
l3.insert(1, 33)
print(l3)

# adding elements to the list using extend - adding multiple elements at end of list
l3.extend([3, 4, 5])
print(l3)

# updating the list
l3[-2] = 11
print(l3)

# removing element from list - Removes the first occurrence of the value.
l3.remove(11)
print(l3)

# removing element from index using pop(index)
l3.pop(1)
print(l3)
l3.pop()
print(l3)

del l3[0]
print(l3)