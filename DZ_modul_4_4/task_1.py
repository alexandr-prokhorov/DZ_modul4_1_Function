# Примеры по разделу *args, **kwargs

# Пример использования *args
def args_processor(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
args = (12,12,12,12,11,12,12,11)
print(f"Сумма всех оценок за 2 месяца обучения {args_processor(*args)}")
print()

# Пример использования **kwargs
def kwargs_processor(**kwargs):
    for k, v in kwargs.items():
        print(f"Key = {k} and value = {v}")
print("Информация о студенте:")
kwargs_processor(name = "Aleksandr", age = 33, country = "Russia", city = "Saratov")

print()

print("Вызов функции еще одним способом")
kwargs = {"name": "Aleksandr", "age": 33, "country": "Russia", "city": "Saratov"}
kwargs_processor(**kwargs)

print()

# Пример использования *args, **kwargs
def args_kwargs_processor(*args, **kwargs):
    print(args,kwargs)
args=("ITtop","student")
kwargs = {"group": "Python426", "name": "Aleksandr", "age": 33, "country": "Russia", "city": "Saratov"}

print("Полная информация о студенте:")
args_kwargs_processor("ITtop","student", group = "Python426", name = "Aleksandr", age = 33, country = "Russia", city = "Saratov")

print("Вывод еще одним способом")
args_kwargs_processor(*args, **kwargs)

