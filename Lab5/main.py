import time

file = open("information.txt", "w+")
Choice = input("Clear file? Yes or No")
if Choice == "Yes" or Choice == "yes":
    file.truncate(0)
while True:
    Name = input("Your Name:")
    Surname = input("Your Surname:")
    Age = input("You Age:")
    Choice = input("Continue? Yes or No")
    file_content = file.read()
    file.write(file_content + f"{Name} {Surname} {Age}\n")
    if Choice == "Yes" or Choice == "yes":
        continue
    elif Choice == "No" or Choice == "no":
        print("Closing...")
        time.sleep(1)
        exit()
    else:
        break


