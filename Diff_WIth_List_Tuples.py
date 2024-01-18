
# list in any Items are Changeable
list = ["A", "B", "C", "D"]
list_num = [1, 2, 3, 4]

# Tuples in All Items Are Static That mean Fixed
color = ("Red", "Green", "Gray", "Pink", "Black")
color_num = (1, 2, 3, 4, 5, 6, 7)

list.insert(2,"Insert Items")
print(list)
list.remove("Insert Items")
print(list)

# Tuples in any items not Changeable
print(list_num)
print(color)
print(color_num)
print(color_num[2])