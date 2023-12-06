our_password = "Pass123"
your_password = ""
num_of_try = 0
num_of_try_max = 5
max_try = ""

while your_password != our_password and max_try != "Reached":
    if num_of_try < num_of_try_max:
        your_password = input("Enter your password: ")
        num_of_try += 1
    else:
        print("Wrong password")
        max_try = "Reached"
        
if max_try == "Reached" :
    print("Account Blocked...")
else :
    print("Access Granted...")
    print("WelCome !")
    print("Your password is " + your_password)