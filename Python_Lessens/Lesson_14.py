v = 0
while v == 0:
    try:
        v = int(input("Введите число v: "))
        v += 5
        print(f"Ваше число {v}")
        # x = 5 / 0
    except ValueError:
        print("Введите лучше число!")
    except ZeroDivisionError:
        print("Деление на нооооль!")
    else:
        print('else')
    finally:
        print('finally')
