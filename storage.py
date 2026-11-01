"""
Project name:Ecommerce_Profit_and_Inventory_calculator
Author:Adhanet Gebretensay
Purpouse:It handles saving and loading inventory data using json.
Date:10/29/2026

"""

import json
from product import Product

def save_inventory(inventory, thefile="inventory_data.json"):
    """ It saves the inventory product to JSON file """
    data_save =  {}
    for key, product in inventory.products_inventory.items():
        data_save[key] = product.to_dict()

    try:
        with open(thefile, "w") as file:
            json.dump(data_save, file, indent=4) 
        print("Inventory saved successfully")
    except IOError:
        print("Error! File can not be saved")

    
def load_inventory(inventory, thefile="inventory_data.json"):
    """ It loads inventory products from JSON """
    try:
        with open(thefile, "r") as file:
            data = json.load(file)

            for key, value in data.items():
                product = Product(
                    name=value["name"],
                    product_id=key,
                    category=value["category"],
                    price=value["price"],
                    cost=value["cost"],
                    stock_quantity=value["stock_quantity"]
                    )
                inventory.products_inventory[key] = product
        print("Inventory is successfully loaded")
    except FileNotFoundError:
        print("No file is found")
    except json.JSONDecodeError:
        print("The data is not formatted correctly")
            
