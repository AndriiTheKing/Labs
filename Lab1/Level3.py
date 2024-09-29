from ast import Index

from unicodedata import numeric
CurrentYear = 2024
CurrentMonth = 9
CurrentDay = 19

Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
NumbersStr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Це лабораторна робота 1. Виконав учень Гавриленко Андрій.")
while True:

    index = 0
    Year_a = []
    Year = 0
    Month_a = []
    Month = 0
    Day_a = []
    Day = 0

    OnlyNum_Array = []


    Name = input("Введіть ім'я: ")
    if Name == "Закрити" or Name == "Close":
        break
    Age_pre = input("Коли ви народилися? (день, місяць, рік) ")

# Creating array without dots
    for x in Age_pre:
        if x in Numbers or x in NumbersStr:
            OnlyNum_Array.append(int(x))
    index1 = 0
    num_sum = 0
    for x in OnlyNum_Array:
        num_sum += x
        index1 += 1

    for i in OnlyNum_Array:
        if index < 2:
            Day_a.append(i)
        elif 2 <= index < 4:
            Month_a.append(i)
        elif  4 <= index < 8:
            Year_a.append(i)
        index += 1

#************************************************
    index_day = 0
    for i in Day_a:
        if index_day == 0:
            Day = i * 10
        elif index_day == 1:
            Day += i
        index_day += 1

    index_month = 0
    for i in Month_a:
        if index_month == 0:
            Month = i * 10
        elif index_month == 1:
            Month += i
        index_month += 1

    index_year = 0
    for i in Year_a:
        if index_year == 0:
            Year = i * 1000
        elif index_year == 1:
            Year = Year + (i * 100)
        elif index_year == 2:
            Year = Year + (i * 10)
        elif index_year == 3:
            Year += i
        index_year += 1
#***************************************************

# # Finding the age numbers in array
#     for x in Age_pre:
#         # if the first 4 character in array is year of born
#         if len(Age_pre) == 4:
#             for b in range(0, 4):
#                 DateOfBorn_Array.append(Age_pre[b])
#             break
#
#
#         if  x not in NumbersStr and index == 4:
#             for b in range(0, index):
#                 DateOfBorn_Array.append(Age_pre[b])
#             break
#
#
#         if x not in NumbersStr and index == 7:
#             for y in range(3, index):
#                 DateOfBorn_Array.append(Age_pre[y])
#             break
#
#         if  x not in NumbersStr and index == 5:
#             for z in range(6, len(Age_pre)):
#                 DateOfBorn_Array.append(Age_pre[z])
#             break
#
#         index += 1
#     #print(Age_pre)                 Testing
#     #print(DateOfBorn_Array)        Testing
#

    #YearOfBirth_pre = DateOfBorn_Array[0] + DateOfBorn_Array[1] + DateOfBorn_Array[2] + DateOfBorn_Array[3]

    #YearOfBirth = int(YearOfBirth_pre)

    DeltaYear = CurrentYear - Year
    if (Month - CurrentMonth) > 0 or ((Month - CurrentMonth) > 0 and (Day - CurrentDay) > 0):
        DeltaYear -= 1


    if 0 < DeltaYear < 120:
        if 2 <= DeltaYear <= 4 or 2 <= DeltaYear % 10 <= 4:
            print(f"Вітаю {Name}, Вам {DeltaYear} роки. Слава Україні!")
        elif DeltaYear == 1 or DeltaYear % 10 == 1 and DeltaYear != 11:
            print(f"Вітаю {Name}, Вам {DeltaYear} рік. Слава Україні!")
        elif DeltaYear > 0:
            print(f"Вітаю {Name}, Вам {DeltaYear} років. Слава Україні!")

    elif DeltaYear < 0:
        print(f"Вітаю {Name},  почекайте трохи ви ще не народилися!")
    else:
        print(f"Press F. Ви мертві! Слава Україні ")

    print(f"Сума чисел: {num_sum}")

