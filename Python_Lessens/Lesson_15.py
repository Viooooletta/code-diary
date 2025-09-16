# try:
#     file = open('text.txt', 'r')  # считывает данные из файла (если его не существует, то выдаст ошибку)
#     # Ошибка!!!
#
#     #Это не выполнелось!
#     file.read()
#     file.close()
# except FileNotFoundError:
#     print('Файл не найден')

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        file.read()
except FileNotFoundError:
    print("Файл не найден")