# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно
# вернуть полученное количество цифр. Например, если
# передали 3456, количество цифр будет 4.

def number_digits (number):
    number_digit = len(str(abs(number)))
    return number_digit

number = int(input("Введите любое число: "))
print(f"Ваше число {number} состоит из {number_digits(number)} цифр")




