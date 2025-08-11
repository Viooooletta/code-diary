data = (1, 2, 3, True, 34.4, 'Hello')
for _ in range(len(data)):
    print(data[_], '\n', end=" ")
print(data[1:4])

nums = [1, 2, 3, 4, 5]
new_data = tuple(nums)
print(new_data)

word = tuple('Hello Mir')
print(word)