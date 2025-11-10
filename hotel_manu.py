# Menu of restaurant
menu = {
    'Pizza': 99,
    'Burger': 45,
    'Pasta': 40,
    'French Fries': 30,
    'Sandwich': 50,
    'Soft Drink': 20,
    'Ice Cream': 25,
    'Salad': 35
}

# Greet
print("Welcome to the Restaurant!")
print("Here is the menu:")
print("Item\t\tPrice")
print('Pizza      :  Rs. 99\nBurger      :  Rs. 45\nPasta       :  Rs. 40\nFrench Fries:  Rs. 30\nSandwich    :  Rs. 50\nSoft Drink  :  Rs. 20\nIce Cream   :  Rs. 25\nSalad       :  Rs. 35\n')

order_total = 0

item1 = input("Enter the item you want to order: ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your order for {item1} has been placed. Total so far: Rs. {order_total}")
else:
    print(f"Sorry, we don't have {item1} on the menu.")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item2 = input("Enter the item you want to order: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your order for {item2} has been added. Total so far: Rs. {order_total}")
    else:
        print(f"Sorry, we don't have {item2} on the menu.")

print(f"\nYour total order amount is Rs. {order_total}")
