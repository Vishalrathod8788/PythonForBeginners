food = ["humburger", "Pizza", "Juice", "Fries", "Sushi", "Sushi", "Sushi"]

price = [55, 25, 20, 30, 15]

food.insert(2, "Sandwich")

# food.extend(price)


print(food.index("Sushi"))

food.remove("Pizza")
print(food)
print(food.count("Sushi"))

random = food.copy() + price.copy()

print(random)