# ==========================
# Book Store Management System
# ==========================

# Initial Inventory
inventory = {
    "Python Programming": {"price": 500.0, "stock": 10},
    "Data Science Guide": {"price": 750.0, "stock": 5},
    "Machine Learning": {"price": 600.0, "stock": 8}
}

while True:
    print("\n========== BOOK STORE MANAGEMENT ==========")
    print("1. Add / Restock Book")
    print("2. View Inventory")
    print("3. Sell Book")
    print("4. Search Book")
    print("5. Update Book Price")
    print("6. Delete Book")
    print("7. Total Inventory Value")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        
        name = input("Enter Book Name: ").title()
        price = float(input("Enter Book Price: "))
        qty = int(input("Enter Quantity: "))

        if price > 0 and qty > 0:
            if name in inventory:
                inventory[name]["stock"] += qty
                inventory[name]["price"] = price
                print("Book Restocked Successfully!")
            else:
                inventory[name] = {"price": price, "stock": qty}
                print("Book Added Successfully!")
        else:
            print("Invalid Price or Quantity!")

    elif choice == "2":
        print("\n------ Current Inventory ------")
        for book, details in inventory.items():
            print(f"Book : {book}")
            print(f"Price: ₹{details['price']}")
            print(f"Stock: {details['stock']}")
            print("--------------------------")

    elif choice == "3":
        name = input("Enter Book Name: ").title()

        if name in inventory:
            qty = int(input("Enter Quantity to Sell: "))

            if qty <= inventory[name]["stock"]:
                inventory[name]["stock"] -= qty
                bill = inventory[name]["price"] * qty
                print(f"Book Sold Successfully!")
                print(f"Total Bill = ₹{bill}")
            else:
                print("Not Enough Stock!")
        else:
            print("Book Not Found!")

    elif choice == "4":
        name = input("Enter Book Name: ").title()

        if name in inventory:
            print("\nBook Found")
            print("Price :", inventory[name]["price"])
            print("Stock :", inventory[name]["stock"])
        else:
            print("Book Not Found!")

    elif choice == "5":
        name = input("Enter Book Name: ").title()

        if name in inventory:
            new_price = float(input("Enter New Price: "))
            inventory[name]["price"] = new_price
            print("Price Updated Successfully!")
        else:
            print("Book Not Found!")

    elif choice == "6":
        name = input("Enter Book Name: ").title()

        if name in inventory:
            del inventory[name]
            print("Book Deleted Successfully!")
        else:
            print("Book Not Found!")

    elif choice == "7":
        total = 0

        for details in inventory.values():
            total += details["price"] * details["stock"]

        print("Total Inventory Value =", total)

    elif choice == "8":
        print("Thank You for Using Book Store Management System.")
        break

    else:
        print("Invalid Choice! Please Enter a Number Between 1 and 8.")