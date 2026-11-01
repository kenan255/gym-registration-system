print("Welcome to our Gym!")

x = input("Enter your name: ")

with open("gym.txt", "a") as f:
    f.write(x + "\n")

k = int(input("Enter your age: "))

if k < 16:
    print("Sorry, you are too young!")

else:
    n = input("Do you want to join our gym? (y/n): ")

    if n == "y":
        print("Choose your membership:")
        print("1 - Monthly")
        print("2 - Yearly")

        m = input("Enter your choice: ")

        if m == "1":
            print("Your membership is Monthly")

        elif m == "2":
            print("Your membership is Yearly")

        else:
            print("Invalid choice")

        print("Thank you for choosing our gym!")

    else:
        print("Thank you for visiting us!")
