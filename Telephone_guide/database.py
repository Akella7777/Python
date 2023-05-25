import view
import csv


def add_data(list):
    with open('book.txt', "a", encoding="utf-8") as file:
        file.write(list)
    print("Телефонная книга обновлена!")


def search():
    str = input("Введите текст для поиска:  ")
    return str


def find_data(name):
    with open('book.txt', "r", encoding="utf-8") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print("Введенных данных не найдено \n")


# сортировка
def sort_db_name():
    wi = open("book.txt", encoding="utf-8")
    k = wi.readlines()
    d = sorted(k)
    th = open("book.txt", "w", encoding="utf-8")
    th.write("".join(d))
    wi.close()
    th.close()


# сортировка по дню рождения
def sort_db_birthday():
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        data.sort(key=lambda x: x[4])
    with open("book.txt", "w", encoding="utf-8") as file:
        file.writelines(data)


def print_name():
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i.split(" ")[1])


def show_guide():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def edited(text: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    birthday = input('Введите дату рождения: ')
    if len(last_name) == 0:
        last_name = text.split(' ')[0]
    if len(first_name) == 0:
        first_name = text.split(' ')[1]
    if len(surname) == 0:
        surname = text.split(' ')[2]
    if len(phone_number) == 0:
        phone_number = text.split(' ')[3]
    if len(birthday) == 0:
        birthday = text.split(' ')
    return last_name + " " + first_name + " " + surname + " " + birthday + " " + phone_number + "\n"


def edit_data(null=None):
    with open('book.txt', 'r', encoding='utf-8') as file:
        tel_book = file.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите изменить: '))
    tel_book[num] = edited(tel_book[num])
    tel_book = '\n'.join(tel_book)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(tel_book)
    print(tel_book)


def del_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        tel_book = file.read()
    tel_book = tel_book.split('\n')
    num = int(input('Введите номер записи, которую хотите удалить: '))
    tel_book.pop(num)
    tel_book = '\n'.join(tel_book)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(tel_book)
    print(tel_book)


def writing_scv():
    f = open("book.txt")
    w = open("book_guide.csv", "w")
    d = sorted(f.readlines())
    w.write("".join(d))
    f.close()
    w.close()
    # with open('book.txt', 'r') as in_file:
    #     stripped = (line.strip() for line in in_file)
    #     lines = (line.split(",") for line in stripped if line)
    #     with open('book_guide.csv', 'w') as out_file:
    #         writer = csv.writer(out_file)
    #         writer.writerow(('last_name', ' first_name', ' surname birthday', ' phone_number'))
    #         writer.writerows(lines)

def writing_txt():
    f = open("book.txt")
    w = open("book_guide.txt", "w")
    d = sorted(f.readlines())
    w.write("".join(d))
    f.close()
    w.close()
    # with open('book.txt', 'r') as in_file:
    #     stripped = (line.strip() for line in in_file)
    #     lines = (line.split(",") for line in stripped if line)
    #     with open('book_guide.txt', 'w') as out_file:
    #         writer = csv.writer(out_file)
    #         writer.writerow(('last_name', ' first_name', ' surname birthday', ' phone_number'))
    #         writer.writerows(lines)
