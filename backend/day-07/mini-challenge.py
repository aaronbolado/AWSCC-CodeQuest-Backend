shop_items = []
menu = True

while (menu): 
    print("\nOptions: " +
        "\n1. Add item to the shopping list" +
        "\n2. View shopping list" + 
        "\n3. Remove item from the shopping list" + 
        "\n4. Quit");
    choice = input("Enter number of your choice: ")

    if choice == '1':
        add_item = input("Enter the item you want to add: ")
        shop_items.append(add_item)
        print(f"{add_item} has been added to your shopping list.")

    elif choice == '2':
        print("Your shopping list: ")
        for item in shop_items:
            print(item)

    elif choice == '3':
        remove_item = input("Enter the item you want to remove: ")
        shop_items.remove(remove_item)
        print(f"{remove_item} has been added to your shopping list.")

    elif choice == '4':
        print("Goodbye!")
        menu = False

    else:
        print("Invalid Input")


