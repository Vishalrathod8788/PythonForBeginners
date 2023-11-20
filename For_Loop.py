for letter in "Hello":
    print(letter)


# Traffic Lite Color 
colors = ["Red", "Yellow", "Green"]

for color in colors:
    print(color)
    if color == "Green":
        print("Go")
        break
    elif color == "Yellow":
        print("Wait")
    else:
        print("Stop")