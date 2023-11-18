def question():
    rules = input("You need to answer every question by yes or no do you understand : ")
    if rules != "yes":
        return print("try again")
    else:
        print("Next Question : ")
    question_1 = input("Are you hungry : ")
    if question_1 != "yes":
        return print("Then let's go for walk")
    else:
        print("Next Question : ")
