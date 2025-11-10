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
for item, price in menu.items():
    print(f"{item:12} : Rs. {price}")
print("\nType 'done' when you are finished ordering.\n")

order_total = 0
order_list = []  # keep track of what user ordered

# Loop for multiple items
while True:
    item = input("Enter the item you want to order: ")

    if item.lower() == "done":  # stop ordering
        break

    if item in menu:
        order_total += menu[item]
        order_list.append(item)
        print(f"✅ {item} added! Total so far: Rs. {order_total}")
    else:
        print(f"❌ Sorry, we don't have {item} on the menu.")

# Final Bill
print("\n------ BILL ------")
for ordered_item in order_list:
    print(f"{ordered_item:12} : Rs. {menu[ordered_item]}")
print("------------------")
print(f"Total Amount   : Rs. {order_total}")
