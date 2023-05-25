def user_input():
    ask = int(input("Выберите ниже:\n "
                    "1 - записать пользователя\n "
                    "2 - поиск\n "
                    "3 - отсортировать\n "
                    "4 - отсортировать по дате рождения\n "
                    "5 - вывести только имена\n "
                    "6 - вывести справочник\n "
                    "7 - изменить данные\n "
                    "8 - удалить данные\n "
                    "9 - выгрузить данные в формате csv\n "
                    "10 - выгрузить данные в формате txt\n "
                    "11 - выйти\n "))
    return ask

def get_info():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    birthday = input('Введите дату рождения: ')
    list = last_name + " " + first_name + " " + surname + " " + birthday + " " + phone_number + "\n"
    return list
