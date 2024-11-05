# Напишите функцию, которая возвращает произведение чисел в
# указанном диапазоне. Границы диапазона передаются в
# качестве параметров. Если границы диапазона перепутаны
# (например, 5 - верхняя граница; 25 - нижняя граница), их нужно
# поменять местами.
from itertools import product


def product_numbers():
    number_range = input("Введите границу диапазона чисел через пробел: ").split()

    number_list = [int(num) for num in number_range]

    if len(number_list) != 2:
        print("Введите 2 числа указывающие верхнюю и нижнюю границу диапазона!")
        return

    lower, upper = sorted(number_list)

    product = 1

    for i in range (lower, upper + 1):
        product *= i
    print(f"Произведение чисел введенного диапазона равна: {product}")

product_numbers()


