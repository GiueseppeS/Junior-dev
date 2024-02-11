menu = ["Croissant", "Espresso", "Cappuccino", "Latte", "Hot Chocolate"]
stock = {"Croissant" : 2, "Espresso" : 0, "Cappuccino" : 6, "Latte" : 15} 
price = {"Croissant" : 2.5, "Espresso" : 2.20, "Cappuccino" : 3, "Latte" : 3}

#case 1
#interacting through the stock and the price
item_value = 0
for item in stock:
    item_value += (stock[item] * price[item])
print(item_value)


#case 2 more difficult
#Checking if the current item in the list is actually in stock and if the number is above 0
item_value = 0
for index, item in enumerate(menu): #need enumerate to check the index of the list
    if item in stock.keys(): #iteracting through the stock key since i'm comparing a string with another
        if stock[item] > 0: #checking the number of value
            item_value += (stock[item] * price[item])
        else:
            print(f"The {menu[index]} is currently not in stock")
    else:
        print(f"The {menu[index]} is currently not in stock")
print(item_value)
