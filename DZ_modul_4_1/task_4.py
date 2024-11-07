# Напишите функцию, которая возвращает минимальное из
# пяти чисел. Числа передаются в качестве параметров.


def check_min_number():
    numbers = input("Введите пять чисел в любом порядке через пробел: ").split()

    number_list = [int(num) for num in numbers]

    min_number = min(number_list)

    # Добавил проверку на ввод 5 чисел
    if len(number_list) != 5:
        print("Введите ровно 5 чисел через пробел!")
        return

    print(f"Минимальное значение из ваших 5 чисел: {min_number}")

check_min_number()
