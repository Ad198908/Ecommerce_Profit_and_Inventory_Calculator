"""
Project name:Ecommerce_Profit_and_Inventory_calculator
Author:Adhanet Gebretensay
Purpouse:To define product class for individual items.
Date:10/29/2026

"""
class Product:
    def __init__(self, name, product_id, category, price, cost, stock_quantity):
        self.name = name
        self.product_id = product_id
        self.category = category
        self.price = price
        self.cost = cost
        self.stock_quantity = stock_quantity

    def to_dict(self):
        return{
            "name":self.name,
            "category":self.category,
            "cost":self.cost,
            "price":self.price,
            "stock_quantity":self.stock_quantity
        }
    
    