old_list = ["Apple", "Banana", "Cherry", "Date"]
print("=======================================")
print("WELCOME TO LIST MANIPULATOR")
print("========================================")

while True:
    print(f"\nYour currentlist:{old_list}")
    print("1.Add item to end (Append)")
    print("2.add item at position (Insert)")
    print("3.Delete item by name(Remove)")
    print("4.Delete item by position(Pop)")
    print("5.Create a new list (Reset)")
    print("6.Delete all items at once(Clear)")
    print("7.EXIT")

    choice = input("\n Choose an option (1-7):")
    
    if choice == "1":
        new_item = input("Enter item name to add:")
        old_list.append(new_item)
        print("Item Added!!!!!")
        
    elif choice == "2":
        new_item = input("Enter item name to insert:")
        position = int(input("Enter position(0,1,2....):"))
        old_list.insert(position, new_item)
        print("Item Inserted!!!!!")
        
    elif choice == "3":
        delt_item = input("Enter exact item name to delete:")
        if delt_item in old_list:
            old_list.remove(delt_item)
            print("Item Removed Successfully!!!!")
        else:
            print("Item not Found!!!!")
            
    elif choice == "4":
        position = int(input("Enter position no.to delete:"))
        pop_item = old_list.pop(position)
        print(f"Removed: {pop_item}")
        
    elif choice == "5":
        old_list = []
        print("\n creating a new list")
        total = int(input("How many items do you want to add to your new list? "))
        for i in range(total):
            item = input(f"Enter item {i+1}: ")
            old_list.append(item)
        print("New list created successfully!")
        
    elif choice == "6":
        old_list.clear()
        print("List completely cleared!!!!")
        
    elif choice == "7":
        print("Thankyou for using list manipulator!😊")
        break
        
    else:
        print("Invalid Option!!!!")






