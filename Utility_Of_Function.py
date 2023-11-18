def per_1(name):
    print(name + " : Hello, how can i help you")


def per_2(name, food, drink):
    name = input("Enter Your Name : ")
    food = input("Enter Your Favorite Food : ")
    drink = input("Enter Your Favorite Drink : ")

    print("My Name is " + name + " I like food : " + food + " i like Drink : " + drink)

per_2("name", "food", "drink")
per_1("name")