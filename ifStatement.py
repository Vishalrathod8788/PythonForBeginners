name_1 = input("What is Your Name : ")
wallet_1 = input("How much money do you have ")

name_2 = input("What is Your Name : ")
wallet_2 = input("How much money do you have ")

name_3 = input("What is Your Name : ")
wallet_3 = input("How much money do you have ")

if wallet_1 > wallet_2 and wallet_1 > wallet_3:
    print(name_1, "is the richest person")
elif wallet_2 > wallet_1 and wallet_2 > wallet_3:
    print(name_2, "is the richest person")
else:
    print(name_3, "is the richest person")
    