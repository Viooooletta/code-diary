# if 5 == 5:
#     print("Пять равно 5 и это правда", end="")
#     print('!!!')
isHappy = False
user_data = int(input("1 Чипсы\n2 Печенье\n3 Суп\nВыберите ваше любимое блюдо: "))

if isHappy and user_data == 1:
    print("Люблю гадкие чепсики")
elif user_data == 2:
    print("Я сладкоежка")
elif user_data == 3:
    print('Я маменькин сынок')
else:
    print('Да я вообще чупакабра')

# if user_data >= 5:
#     print("Мы на месте")
#     if user_data > 10:
#         print("Число больше 10")
# else:
#     print("Число меньше чем 5")
data = input()
number = 5 if data == "Five" else 0