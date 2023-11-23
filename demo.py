our_pass = "123Pass"
your_pass = ""
num_of_try = 0
num_of_try_limit = 3
max_try = "not reached..."

while your_pass != our_pass and max_try != "Reached" :
    if num_of_try < num_of_try_limit :
        your_pass = input("Enter Your Password...")
        num_of_try += 1
    else :
        print("Wrong Password...")
        max_try = "Reached"
if max_try == "Reached" :
    print("Account Blocked...")
else :
    print("Access Granted...")
    print("Welcome !")
    