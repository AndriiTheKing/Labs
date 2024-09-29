
print("—————————————————————————————————————————————————\nПравила:\n1) Вводити тільки числа\n2) Перше число повинно "
      "бути меншим за друге.\n—————————————————————————————————————————————————")
while True:

    Str_S = input("Введіть перше число: ")
    Str_F = input("Введіть друге число: ")
    Str_D = input("Введіть третє число: ")

    # Якщо введені дані є цифрами від 0 до 9, то дані заносяться в окремі змінні. Якщо перше число більше за друге то починаємо з початку.
    if Str_S.isdigit() and Str_F.isdigit() and Str_D.isdigit():
        S = int(Str_S)
        F = int(Str_F)
        D = int(Str_D)

        if F < S:
            print("Неправильно введені дані. Перше число повинно бути меншим за друге.")
            continue
        if D == 0:
            print("Неправильно введені дані. Недопустимий нуль")
            continue
        for i in range(S, F + 1):
            if i % D == 0:
                print(i)
    else:
        print("Некоректні дані. Потрібно вводити тільки числа")
        continue

    # Цикл після завершення виконання програми
    close_option = False
    while True:

        print("1.Продовжити.")
        print("2.Завершити.")
        choice = input("Введіть цифру:")
        print("—————————————————————————————————————————————————")
        if choice == "1":
            break
        elif choice == "2":
            print("Завершення...")
            close_option = True
            break
        else:
            print("Некоректні дані. Введіть 1 або 2.")
            continue
    if close_option:
        break