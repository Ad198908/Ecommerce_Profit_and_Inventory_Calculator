"""
    Program name: Ecommerce_Profit_and_Inventory_Calculator
    Author: Adhanet Gebretensay
    Purpose:
    Date:Septempber 16/2026

    """
STORE_INFO = ("Admart", "USD")
inventory ={

     "AD-PRODUCT-001" : {
          "name": "Canvas Wall Art",
          "category": "Wall Art",
          "cost":8.40,
          "price":12.50,
          "stock_quantity": 100
     }, 

     "AD-PRODUCT-002":{
           "name": " Candle",
            "category": "home appliance",
            "cost":9.40,
            "price":16.50,
            "stock_quantity": 180
          
     },

    "AD-PRODUCT-003": {
       "name": "flower",
       "category":"kitchin material" ,
       "cost":30.99,
       "price": 39.50,
       "stock_quantity":100

      }
}  
sales_history = []

def viewInventory(inventory):
    print("Current Inventory")
     
    if not inventory:
        print("The inventory is empty")
        return
    else:
        for key, value in inventory.items():
            product = value ["name"]
            category = value["category"]
            price = value["price"]
            stock_quantity = value["stock_quantity"]
            print(f" Name:{product}")
            print(f"Price: {price}, Catagory: {category}, Stock: {stock_quantity}")
            print("-"*30)

def updeatInventory(inventory):
    print("---------Update Invontory----------")
    Id = input("Please enter the product id ")        
    Id = Id.strip().upper()
    if (Id in inventory):
        print("Please change the inventory ID, it already exists.")
        return
    else:
        name= input("Please enter the product name ").strip()
        price = float(input("Please enter the product price "))
        cost = float(input("Please enter the product cost "))
        category = input("Please enter the product category ").strip()
        stock_quantity = int(input("Please enter the product stock_quantity "))

        inventory[Id] = {
            "name": name,
            "price": price,
            "cost": cost,
            "category": category,
            "stock_quantity":stock_quantity
            }

        print("Product added sucssesfully")

def recordSales(inventory, sales_history):

    print("Record Sales \n")
    quantity_bought = int(input("How many items are bought?"))
    if quantity_bought == 0:
        print("quantity_bought can not be empty")
        return

    P_id = input("Please enter product Id").strip().upper()

    if not inventory:
        print("Can not record sales")
        return

    if P_id not in inventory:
        print("There is no product with that ID")
        return
    else:
        product = inventory[P_id]
        stock = product["stock_quantity"]
        price =  product["price"]
        cost = product["cost"]
        print(f"Selected {product["name"]}")
        if quantity_bought <= stock:
            stock = stock - quantity_bought
            reveniue = quantity_bought * price
            profit = reveniue - (quantity_bought*cost)

            sales_history.append(               
                {
            "quantity_bought": quantity_bought,
            "reveniue": reveniue,
            "profit": profit
                }
            )
            print("Logged Succcessfully")
            print(sales_history)


#state flag
isRunning = True

while isRunning:
    print("-"*50)
    print("1. View Invontory")
    print("2. Update Invontory")
    print("3. Record Sales")
    print("4. View Profit")
    print("5. Exit")
    print("-"*50)
    userChoice = int(input("Enter your choice 1-5 \n"))
    
    if userChoice == 1:
        viewInventory(inventory)       
    elif userChoice == 2:
        updeatInventory(inventory)          
    elif userChoice == 3:

       recordSales(inventory , sales_history)          
    elif userChoice == 4:
          print("View Profit Coming Soon\n") 
    elif userChoice == 5:
        isRunning = False
    else:
        print("Please Enter 1-5\n")  
    
        
