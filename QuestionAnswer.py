def question():
    rules = input("You need to answer every question by yes or no do you understand : ")
    if rules != "yes":
        return print("try again")
    else:
        print("Next Question : ")
