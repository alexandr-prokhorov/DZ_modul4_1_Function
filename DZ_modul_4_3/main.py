from utils import get_reg_data, reg_check

users_list=[]

patterns = get_reg_data()

while len(users_list) < 3:
    user_data_list = []

    while True:
        input_name = input("Введите имя пользователя: ").title().strip()
        name = reg_check(input_name, patterns["name"], users_list)
        if name:
            user_data_list.append(name)
            print("Имя принято")
            break
        else:
            print("Ошибка: содержит неподходящие символы.")

    while True:
        input_surname = input("Введите фамилию пользователя: ").title().strip()
        surname = reg_check(input_surname, patterns["surname"], users_list)
        if surname:
            user_data_list.append(surname)
            print("Фамилия принята")
            break
        else:
            print("Ошибка: содержит неподходящие символы.")

    while True:
        input_telephone = input("Введите Ваш номер телефона в формате +***(**)*******: ").strip()
        telephone = reg_check(input_telephone, patterns["telephone"], users_list, 2)
        if telephone:
            user_data_list.append(telephone)
            print("Телефон принят")
            break
        else:
            print("Телефон не соответствует формату или уже существует.")

    while True:
        input_mail = input("Введите ваш email на Яндексе: ").strip()
        mail = reg_check(input_mail, patterns["mail"], users_list, 3)
        if mail:
            user_data_list.append(mail)
            print("Почта принята")
            break
        else:
            print("Почта должна содержать @yandex.ru или уже существует.")

    user_duplicate = any(
        user[2] == user_data_list[2] or
        user[3] == user_data_list[3]
        for user in users_list
    )

    if user_duplicate:
        print("Ошибка: пользователь с такими данными уже существует. Попробуйте снова.")
    else:
        users_list.append(user_data_list)
        print("Пользователь добавлен.")

print("Готовый список пользователей: ")
for user in users_list:
    print(user)