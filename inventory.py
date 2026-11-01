"""
Project name:Ecommerce_Profit_and_Inventory_Calculator
Author:Adhanet Gebretensay
Purpose:To manage inventory add items and record salse class .
Date:10/29/2026

"""
from product import Product

class Inventory:

    def __init__(self):
        self.sales_history = []
        self.products_inventory = {}

    def add_product(self, product):
        """ They add product object to inventory """
        self.products_inventory[product.product_id] = product

    def view_inventory(self):
        """This function lets the store owner view the inventory
        """
        print("Current Inventory")
        
        if not self.products_inventory:
            print("The prodct inventory is empty")
            return
        else:
            for key, value in self.products_inventory.items():
                product = value.name
                category = value.category
                price = value.price
                stock_quantity = value.stock_quantity
                print(f" Name:{product}")
                print(f"Price: {price}, Catagory: {category}, Stock: {stock_quantity}")
                print("-"*30)

    def record_sales(self, product_id, quantity_bought):
        """
            Record product inventory, and sales history.
            Args:
                inventory (dictionary):Product inventory details.
                sales_history (list):The list containing sales details.
            """

        print("Product Record Sales \n")
        
        if quantity_bought == 0:
            print("quantity bought can not be empty")
            return False

        if not self.products_inventory:
            print("Can not record sales")
            return False

        if product_id not in self.products_inventory:
            print("There is no product with that ID")
            return False
        else:
            product = self.products_inventory[product_id]
            stock = int(product.stock_quantity)
            price =  float(product.price)
            cost = float(product.cost)
            print(f"Selected {product.name}")


            if quantity_bought <= stock:
                new_stock = stock - quantity_bought
                product.stock_quantity = new_stock
                revenue = quantity_bought * price
                profit = revenue - (quantity_bought*cost)
                cost = quantity_bought * cost

                self.sales_history.append(               
                    {
                    "quantity_bought": quantity_bought,
                    "revenue": revenue,
                    "profit": profit,
                    "cost": cost,
                    }
                )
                print("Logged Succcessfully")
                print(self.sales_history)
                return True
            else:
                return False

    def get_Summary(self):
        """
        This function shows view product sales history.
        Args:
            sales_history (list): product sales detail.
        """
        print("---------getSummary----------")
        if not self.sales_history:
            print("Sales history is empty")
            return
        else:
            total_cost = 0.0
            total_profit = 0.0
            total_revenue = 0.0

            for sales_record in self.sales_history:
                total_revenue = total_revenue + sales_record["revenue"]
                total_cost = total_cost + sales_record['cost']
                total_profit = total_profit + sales_record["profit"]

            print("Sales Summary!")
            print(f"Revenue = {total_revenue}")
            print(f"Cost = {total_cost}" )
            print(f"Profit = {total_profit}")


    

