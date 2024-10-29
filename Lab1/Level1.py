while True:

    Name = input("Введіть ім'я: ")
    if Name == "Закрити" or Name == "Close":
        break
    Age_pre = input("Скільки вам років? ")
    Age = int(Age_pre)
    if Age == 1:
        print(f"Вітаю {Name} ({Age} рік). Слава Україні!")
    elif 0 < Age < 5:
     print(f"Вітаю {Name} ({Age} роки). Слава Україні!")
    else:
      print(f"Вітаю {Name} ({Age} років). Слава Україні!")
