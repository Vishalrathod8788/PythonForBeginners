our_password = "Pass123"
your_password = ""
num_of_try = 0
num_of_try_max = 3
max_try = "not Reached"

while your_password != our_password and max_try != "Reached ":
    if num_of_try < num_of_try_max:
        your_password = input("Enter your password: ")
        num_of_try += 1
        if your_password != our_password:
            print("Wrong password")
            print("You have " + str(num_of_try_max - num_of_try) + " try left")
            max_try = "Reached"

        else:
            print("Welcome")            