# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата,
# символ и переменную логического типа:
# если она равна True, квадрат заполненный;
# если False, квадрат пустой.
print("Давайте нарисуем квадрат из выбранного символа!")
def draw_square():

    side_length = int(input("Введите длину квадрата: "))
    symbol = input("Введите символ из которого нарисовать квадрат: ")

    filled_input = input("Нарисовать заполненный квадрат? (да/нет): ").strip().lower()
    filled = filled_input == "да"

    for i in range (side_length):
        if filled or i == 0 or i == side_length - 1:
            print(symbol * side_length)
        else:
            print(symbol + " " * (side_length - 2) + symbol)

draw_square()
