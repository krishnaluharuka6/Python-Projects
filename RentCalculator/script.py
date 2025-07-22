# input = total rent, total food cost, electricity unit spend, charge per unit, number of people

# output total amount you've to pay



rent = int(input("Enter the flat rent"))
food = int(input("Enter the amount of food ordered"))
electricity_spend = int(input("Enter the total of electricity spend"))
charge_per_unit = int(input("Enter the charge per unit"))
total_number_of_people = int(input("Enter the number of persons living in the flat"))


electricity_cost = electricity_spend * charge_per_unit

per_unit_cost = int((rent + food + electricity_cost)/total_number_of_people)
print(f"Each person will pay Rs. {per_unit_cost}")

