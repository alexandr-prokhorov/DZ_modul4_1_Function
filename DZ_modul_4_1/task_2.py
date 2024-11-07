# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все четные числа между ними
print("Программа для вывода четных чисел из вашего диапазона!")
def display_even_numbers():
    start_number = int(input("Введите начальное число диапазона: "))
    end_number = int(input("Введите конечное число диапазона: "))

    if start_number % 2 != 0:
        start_number += 1

    for num in range (start_number,end_number + 1, 2):
        print(num)

display_even_numbers()