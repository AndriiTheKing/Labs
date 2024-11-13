import csv


fields = ['Name', 'Surname', 'Age']


rows = []





import time

while True:
    Name = input("Your Name:")
    Surname = input("Your Surname:")
    Age = input("You Age:")
    Choice = input("Continue? Yes or No")

    rows.append([Name, Surname, Age])
    with open("information.csv", 'w') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

        csvwriter.writerows(rows)


    if Choice == "Yes" or Choice == "yes":
        continue
    elif Choice == "No" or Choice == "no":
        print("Closing...")
        time.sleep(1)
        exit()
    else:
        break
