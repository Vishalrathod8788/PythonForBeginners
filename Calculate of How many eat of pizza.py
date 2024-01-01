name_1 = input("What is your name ")
name_2 = input("What is your name ")
name_3 = input("What is your name ")

Slice_in_the_Pizza = input("Slice in the pizza ")
Price_of_the_Pizza = input("Price of the pizza ")

percetage_ate_by_person_1 = input(name_1 + " Percentage ate by person 1 ")
percetage_ate_by_person_2 = input(name_2 + " Percentage ate by person 2 ")
percetage_ate_by_person_3 = input(name_3 + " Percentage ate by person 3 ")

number_of_slices_ate_by_person_1 = float(percetage_ate_by_person_1) * float(Slice_in_the_Pizza)
number_of_slices_ate_by_person_2 = float(percetage_ate_by_person_2) * float(Slice_in_the_Pizza)
number_of_slices_ate_by_person_3 = float(percetage_ate_by_person_3) * float(Slice_in_the_Pizza)

price_payed_by_name_1 = float(percetage_ate_by_person_1) * float(Price_of_the_Pizza)
price_payed_by_name_2 = float(percetage_ate_by_person_2) * float(Price_of_the_Pizza)
price_payed_by_name_3 = float(percetage_ate_by_person_3) * float(Price_of_the_Pizza)

print(name_1 +" have eat "+ str(number_of_slices_ate_by_person_1) + " Slices and have payed "+ str(price_payed_by_name_1)+"$ meal " )
print(name_2 +" have eat "+ str(number_of_slices_ate_by_person_2) + " Slices and have payed "+ str(price_payed_by_name_2)+"$ meal " )
print(name_3 +" have eat "+ str(number_of_slices_ate_by_person_3) + " Slices and have payed "+ str(price_payed_by_name_3)+"$ meal " )

