n = input("Enter Digit...")




for i in range(int(n)):
    for j in range(int(n)-i):
        print(" ", end="    ")
    for k in range(i):
        print("*", end="    ")
    print()
    print()

for i in range(int(n)):
    for j in range(i):
        print("*", end="    ")
    print()
    print()