

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
    for j in string:
        if j != " ":
            if j == "m" or j == "M":
                pass
            elif j == "a" or j == "A":
                pass
            elif j == "x" or j == "X":
                option_l.append("max")
            else:
                option_l.append(j)

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
    main_command = input("Команди:\n"
                    "1) Почати.\n"
                    "2) Допомога.\n"
                    "3) Закінчити.\n:")
    if main_command == "1":
        while not bIsClose:

            text = input("Що робимо?\n:")
            temp_l = []
            for i in text:
                if i != " ":
                    if i == "m" or i == "M":
                        pass
                    elif i == "a" or i == "A":
                        pass
                    elif i == "x" or i == "X":
                        temp_l.append("max")
                    else:
                        temp_l.append(i)

            print(f"{temp_l[0]} {temp_l[1] } {temp_l[2]} = {calculate(text)}")

            continue_command = input("1) Продовжити\n2) Назад\n:")
            if continue_command == "1":
                continue
            elif continue_command == "2":
                break

    elif main_command == "2":
        print(help_text)
        option = input("1) Назад\n:")
        if option == "1":
            continue
    elif main_command == "3":
        break


