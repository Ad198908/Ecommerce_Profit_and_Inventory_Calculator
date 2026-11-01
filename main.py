"""
    Program name: Ecommerce_Profit_and_Inventory_Calculator
    Author: Adhanet Gebretensay
    Purpose: A CLI application to calculate the profit ,cost ,and revenue of an ecommerice business.
    Date:Septempber 16/2026

"""
from inventory import Inventory
from product import Product
from storage import load_inventory , save_inventory



STORE_INFO = ("Admart", "USD")

def main():
    my_inventory = Inventory()
    load_inventory(my_inventory)

     #state flag
    isRunning = True

    while isRunning:
        print("-"*50)
        print(f"Welcome to {STORE_INFO[0]}")
        print("1. View Invontory")
        print("2. Update Invontory - Add Product")
        print("3. Record Sales")
        print("4. View Profit Summary")
        print("5. Save and Exit")
        print("-"*50)

        try:
            userChoice = int(input("Enter your choice 1-5 \n"))
        except ValueError:
            print("Please enter a valid number \n")
            continue
        
        if userChoice == 1:
            my_inventory.view_inventory()       
        elif userChoice == 2:
            p_id = input("Please enter the product ID").strip().upper()
            if p_id in my_inventory.products_inventory:
                print("The product ID exists. Please use another one")
                continue
            name = input("Please enter the product name").strip()
            category = input("Please enter the product category").strip()
            cost = input("Please enter the product cost")
            price  = input("Please enter the product price")
            stock = input("Please enter the product stock")
            new_product = Product(
                name=name,
                product_id=p_id,
                category=category,
                cost=cost,
                price=price,
                stock_quantity= stock
            )
            my_inventory.add_product(new_product)
            print("Product Added Successfully!")       
        elif userChoice == 3:
            p_id = input("Please enter the product ID").strip().upper()
            quan = int(input("How many items were bought?"))
            my_inventory.record_sales(product_id=p_id,quantity_bought=quan)
        elif userChoice == 4:
            my_inventory.get_Summary()
        elif userChoice == 5:
            save_inventory(my_inventory)
            isRunning = False
            print("Exiting Application. Thank you")
        else:
            print("Please Enter 1-5\n")  
        
if __name__ == "__main__":
    main()
