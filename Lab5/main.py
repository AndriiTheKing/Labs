import time


while True:

    with open("information.txt", "a") as file:
        Name = input("Your Name:")
        Surname = input("Your Surname:")
        Age = input("You Age:")
        file.write(f"{Name} | {Surname} | {Age}\n")


    Choice = input("Continue? Yes or No")
    if Choice == "Yes" or Choice == "yes":
        continue
    elif Choice == "No" or Choice == "no":
        print("Closing...")
        time.sleep(1)

        break


