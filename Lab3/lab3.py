

def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(base, divider):
    if divider != 0:
        return base / divider
    global err
    err = True
    return 0

def power(base :int, exponent :int):
    return pow(base, exponent)

def maximum(a, b):
    if a > b or a == b:
        return a
    return b

def calculate(string):
    option_l = []
    for i in string:
        if i != " ":
            option_l.append(i)

    if len(option_l) > 0:
        if "^" in option_l:
            index = option_l.index("^")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return power(a, b)

        if "+" in option_l:
            index = option_l.index("+")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return summ(a, b)

        if "-" in option_l:
            index = option_l.index("-")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return diff(a, b)

        if "*" in option_l:
            index = option_l.index("*")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return mult(a, b)

        if "/" in option_l:
            index = option_l.index("/")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return divide(a, b)

        if "max" in option_l:
            index = option_l.index("max")
            if len(option_l) > index:
                if option_l[0].isdigit() and option_l[index + 1].isdigit():
                    a = int(option_l[0])
                    b = int(option_l[index + 1])
                    return maximum(a, b)

err = False
err_text = "Виникла помилка. Неправилно всесені дані. Перечитайте правила."


bIsClose = False

help_text = ("Правила:\n"
             "1) Не ділити на нуль.\n"
             "Синтаксис: {число а} (оператор) {число b} Приклад: 1 + 2\n"
             "Оператори:\n"
             " + - Додає числа.\n"
             " - - віднімає числа\n"
             " * - перемножує числа між собою\n"
             " / - ділить перше число на друге\n"
             " max - знаходить максимальне число з 2 введених\n"
             " ^ - підносить перше число в степінь другим числом\n")
while True:
    command = input("Команди:\n"
                    "1) Почати.\n"
                    "2) Допомога.\n"
                    "3) Закінчити.\n:")
    if command == "1":
        while not bIsClose:

            text = input("Що робимо?\n:")
            temp_l = []
            for i in text:
                if i != " ":
                    temp_l.append(i)

            print(f"{temp_l[0]} {temp_l[1] } {temp_l[2]} = {calculate(text)}")

            temp_command = input("1) Продовжити\n2) Назад\n:")
            if temp_command == "1":
                continue
            elif temp_command == "2":
                break

    elif command == "2":
        print(help_text)
        option = input("1) Назад\n:")
        if option == "1":
            continue
    elif command == "3":
        break

#@todo : Доробити цикл фор томущо max не читає
