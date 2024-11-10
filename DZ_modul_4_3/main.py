from utils import get_reg_data, reg_check

users_list=[]

patterns = get_reg_data()

while len(users_list) < 3:
    user_data_list = []

    while len(user_data_list) < 1:
        input_name = input("Введите имя пользователя: ").title().strip()
        name = reg_check(input_name, patterns["name"], users_list)
        if name:
            user_data_list.append(name)
            print("Имя принято")
        else:
            print("Ошибка: содержит не подходящие символы")

    while len(user_data_list) < 2:
        input_surname = input("Введите фамилию пользователя: ").title().strip()
        surname = reg_check(input_surname, patterns["surname"], users_list)
        if surname:
            user_data_list.append(surname)
            print("Фамилия принята")
        else:
            print("Ошибка: содержит не подходящие символы")

    while len(user_data_list) < 3:
        input_telephone = input("Введите Ваш номер телефона в формате +***(**)*******: ").strip()
        telephone = reg_check(input_telephone, patterns["telephone"], users_list)
        if telephone:
            user_data_list.append(telephone)
            print("Телефон принят")
        else:
            print("Телефон не соответствует формату +***(**)*******")
    while len(user_data_list) < 4:
        input_mail = input("Ведите ваш email на яндексе: ").strip()
        mail = reg_check(input_mail, patterns["mail"], users_list)
        if mail:
            user_data_list.append(mail)
            print("Почта принята")
        else:
            print("Почта должна содержать @yandex.ru")

    users_list.append(user_data_list)

print("Готовый список пользователей: ")

for user in users_list:
    print(user)