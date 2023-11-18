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
    question_2 = input("Do you want to eat at a restorer : ")
    if question_2 != "yes":
        return print("come eat at my place ")
    else:
        print("Next Question : ")
    question_3 = input("Do you want to eat Pizza : ")
    if question_3 != "yes":
        return print("let's go eat burger then ")
    else:
        print("let's go eat pizza ")

question()