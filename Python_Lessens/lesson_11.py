data = set('helloooo')
data1 = {5, 75, 345, 312, 5,  5 }
data1.add(5)
data1.remove(5)
print(data)
data.pop()
print(data)
print(data1)
data.pop()

new_data = frozenset([5, 75, 345, 312, 5,  5, True ])

print(new_data)
