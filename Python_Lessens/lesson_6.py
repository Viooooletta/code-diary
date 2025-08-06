# for i in range(100, 10, -1):
#     print(i)
word = 'Hello Mir'
count = 0
for i in word:
    if i == 'l':
        print(" ", end='')
    else:
        print(i, end='')
        count += 1
print('\n', 'Количество букв: ',count, sep='')


isHappy = True
while isHappy:
    if input('Как настроение?\n') == 'Норм':
        isHappy = False

for _ in range (1, 11):
    print (_)
    if _ == 5:
        break
print ("Все")

for _ in range (1, 11):
    print (_)
    if _ == 5:
        continue
found = False
l = 0
word = input()
for m in word:
    if m == 'l':
        l += 1
if l > 0:
    found = True
print(found, l)