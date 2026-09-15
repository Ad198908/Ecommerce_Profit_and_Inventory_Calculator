"""
    Program name: Ecommerce_Profit_and_Inventory_Calculator
    Author: Adhanet Gebretensay
    Purpose:
    Date:Septempber 16/2026

    """
STORE_INFO = ("Admart", "USD")

# print("-"*50)
# print(f"WELCOME TO {STORE_INFO[0]}")
# print("1. View Inventory")
# print("2. Update Inventory")
# print("3. Record Sales")
# print("4. View profit")
# print("5. Exit")
# print("-"*50)

# choice = input("please enter your choice ")
# print(choice)

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
    
    if (userChoice) == 1:
         print("STUB View Inventory. Coming Soon\n")
    elif(userChoice)== 2:
         print("Update Inventory Coming Soon\n")
    elif(userChoice)== 3:
         print("Record Sales Coming Soon\n")
    elif(userChoice)== 4:  
    
          print("View Profit Coming Soon\n")
    
    elif(userChoice)== 5:
        isRunning = False
    
    else:
        print("Please Enter 1-5")

               
    
        
