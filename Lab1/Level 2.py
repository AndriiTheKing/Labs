from ast import Index

from unicodedata import numeric
CurrentYear = 2024
while True:

    ListOfChars = []
    index = 0
    DateOfBorn_Array = []

    Name = input("Введіть ім'я: ")
    if Name == "Закрити" or Name == "Close":
        break
    Age_pre = input("Коли ви народилися? ")


# Finding the age numbers in array
    for x in Age_pre:
        # if the first 4 character in array is year of born
        if len(Age_pre) == 4:
            for b in range(0, 4):
                DateOfBorn_Array.append(Age_pre[b])
            break
        elif x == "." and index == 4:
            print("first")
            for b in range(0, index):
                DateOfBorn_Array.append(Age_pre[b])
            break


        elif x == "." and index == 7:
            print("second")
            for y in range(3, index):
                DateOfBorn_Array.append(Age_pre[y])
            break

        elif x  == "." and index == 5:
            print("third")
            for z in range(6, len(Age_pre)):
                DateOfBorn_Array.append(Age_pre[z])
            break

        index += 1



    YearOfBirth_pre = DateOfBorn_Array[0] + DateOfBorn_Array[1] + DateOfBorn_Array[2] + DateOfBorn_Array[3]
    YearOfBirth = int(YearOfBirth_pre)

    if 0 < (CurrentYear - YearOfBirth) < 120:
        if 2 <= (CurrentYear - YearOfBirth) <= 4 or 2 <= (CurrentYear - YearOfBirth) % 10 <= 4:
            print(f"Вітаю {Name}, Вам {CurrentYear - YearOfBirth} роки. Слава Україні!")
        elif (CurrentYear - YearOfBirth) == 1 or (CurrentYear - YearOfBirth) % 10 == 1 and (
                CurrentYear - YearOfBirth) != 11:
            print(f"Вітаю {Name}, Вам {CurrentYear - YearOfBirth} рік. Слава Україні!")
        elif (CurrentYear - YearOfBirth) > 0:
            print(f"Вітаю {Name}, Вам {CurrentYear - YearOfBirth} років. Слава Україні!")

    elif (CurrentYear - YearOfBirth) < 0:
        print(f"Вітаю {Name},  почекайте трохи ви ще не народилися!")
    else:
        print(f"Press F. Ви мертві! Слава Україні ")

    DateOfBorn_Array.clear()
