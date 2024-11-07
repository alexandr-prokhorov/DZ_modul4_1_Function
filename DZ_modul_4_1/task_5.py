# Напишите функцию, которая возвращает произведение чисел в
# указанном диапазоне. Границы диапазона передаются в
# качестве параметров. Если границы диапазона перепутаны
# (например, 5 - верхняя граница; 25 - нижняя граница), их нужно
# поменять местами.


def product_numbers():
    number_range = input("Введите границу диапазона чисел через пробел: ").split()

    number_list = [int(num) for num in number_range]

    if len(number_list) != 2:
        print("Введите 2 числа указывающие верхнюю и нижнюю границу диапазона!")
        return

    lower, upper = sorted(number_list)

    product_digit = 1

    for i in range (lower, upper + 1):
        product_digit *= i
    print(f"Произведение чисел введенного диапазона равна: {product_digit}")

product_numbers()


