
menu = {
    "Pizza" : 80,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad" : 70,
    "Coffee" : 80
}

print("""Welcome to our restaurant. Here's the menu:
      Pizza : Rs40
      Pasta: Rs50
      Burger: Rs60
      Salad: Rs70
      Coffeee: Rs80""")


order_total = 0

item1 = input("Enter the first item you want to order ").capitalize()
if item1 in menu:
    order_total += menu[item1]
    print(f"Order of {item1} has been added")
else:
    print("Your order is not available in our restaurant")



order2 = input("Do you want to order anything else? (Yes/No)")
if order2.capitalize() == 'Yes':
    item2 = input("Enter the second item you want to order").capitalize()
    if item2.capitalize() in menu:
        order_total += menu[item2]
        print(f"Order of {item2} has been added")
    else:
        print("Your order is not available in our restaurant")
        
print(f"Your total amount is {order_total}")