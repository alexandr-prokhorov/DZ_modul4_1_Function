# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
#  Bill Gates


def display_text():
    name_autor = "Bill Gates"
    print("“Don't compare yourself with anyone in this world…")
    print("if you do so, you are insulting yourself.”")
    #Сделал отступ для оформления как в задании.
    print(f"{name_autor:>50}")

display_text()



