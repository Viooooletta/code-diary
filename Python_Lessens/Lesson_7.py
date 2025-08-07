nums = [3, 45, 56] # Пустой список
print('Список: ', end='')
for _ in nums:
    print(_, end=' ')
nums.append(nums[-1] + 1)

print('\nОбновленный список: ', end='')
for _ in nums:
    print(_, end=' ')

nums.insert(2, nums[1] + 1)

print('\nОбновленный список: ', end='')
for _ in nums:
    print(_, end=' ')

newNums = []
n = 2
m = nums[n]
while m != nums[n + 1]:
    m += 1
    newNums.append(m)

nums[n + 1: n + 1] = newNums


print('\nОбновленный список: ', end='')
for _ in nums:
    print(_, end=' ')

nums.append(True)
nums.sort()
nums.reverse()
nums.pop()
nums.remove(54)
# nums.clear()
print('\nКоличество троек в списке:', nums.count(3))
print('Обновленный список: ', end='')
for _ in nums:
    print(_, end=' ')
print('\nДлина всего списка: ', len(nums))

print('Сгенерируем новый список: ')
listick = [a for a in range(10)]
print (listick)


print(' '.join([str(a) for a in listick]))

strokaNeStroka = ['Привет', 'Я', 'Листик']
print(' '.join(strokaNeStroka))
str = 'jefgVjfnhVonVij'
print(str.split('V'))
# nums = [1, 2, 3, 7]
# nums1 = [1, 2, 3, 3, 43, 7]
# new = [4, 5, 6]
#
# n = nums.index(3) + 1
# nums[n:n] = new
# print("Списочек 1:", end=" ")
# for _ in nums:
#     print(_, end=" ")
#
# n = nums1.index(3) + 1
# m = nums1.index(7)
# nums1[n:m] = new
#
# print("\nСписочек 2:", end=" ")
# for _ in nums1:
#     print(_, end=" ")
