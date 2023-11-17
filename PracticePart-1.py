price_product_1 = input("What is the Price of the Product ")
quantity_product_1 = input("What is the Quantityof the Product ")
price_product_2 = input("What is the Price of the Product ")
quantity_product_2 = input("What is the Quantityof the Product ")
price_product_3 = input("What is the Price of the Product ")
quantity_product_3 = input("What is the Quantityof the Product ")

result_product_1 = float(price_product_1) * int(quantity_product_1)

print(result_product_1)

result_product_2 = float(price_product_2) * int(quantity_product_2)

print(result_product_2)

result_product_3 = float(price_product_3) * int(quantity_product_3)

print(result_product_3)

print("Your Final Price is "+ str(result_product_1 + result_product_2 + result_product_3))
