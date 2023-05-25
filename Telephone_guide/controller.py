import view
import database


def main(Q=None):
    while True:
        ask = view.user_input()
        if ask == 1:
            list = view.get_info()
            database.add_data(list)
        elif ask == 2:
            name = database.search()
            database.find_data(name)
        elif ask == 3:
            database.sort_db_name()
        elif ask == 4:
            database.sort_db_birthday()
        elif ask == 5:
            database.print_name()
        elif ask == 6:
            database.show_guide()
        elif ask == 7:
            database.edit_data()
        elif ask == 8:
            database.del_data()
        elif ask == 9:
            database.writing_scv()
        elif ask == 10:
            database.writing_txt()
        elif ask == 11:
            break
        else:
            print('Выбран не заданный символ. Повторите попытку')


main()
