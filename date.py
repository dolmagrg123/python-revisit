menu = {
        "Wings": {
            "Course": "Appetizer", 
            "Ingredients": ["chicken", "garlic", "BBQ Sauce"], 
            "Price": 15, "Description": "These are the best wings in the world!"
            },
        "Steak and Eggs": {
            "Course": "Main", 
            "Ingredients": ["Wagyu", "Eggs", "Salt and Pepper"], 
            "Price": 45, 
            "Description": "High grade Wagyu with Free range organic eggs from Japan"
            },
        "Sushirito": {
            "Course": "Main", 
            "Ingredients": ["Salmon", "Rice", "Nori"], 
            "Price": 25, 
            "Description": "Freshly imported salmon from coldest Japanese oceans"
            },
        "Kakigori": {
            "Course": "Dessert", 
            "Ingredients": ["Shaved Ice", "Condensed Milk", "Strawberry"], 
            "Price": 10, 
            "Description": "Refreshing dessert"},
}

name_date = input("Who is on a date with you?")
budget = int(input("What is your budget for the date?"))

def order_item(menu,budget):
    total_bill = 0
    print(menu)
    while True:
        response = input("Would you like to order? (Y/N)")
        count = 0
        if response == 'Y' or response == 'y' :
            count = count + 1
            food = input("What would you like to eat?")
            budget = budget - int(menu[food]["Price"])
            total_bill = total_bill + int(menu[food]["Price"])
            print("You have", budget , "dollars remaining in your budget")
        else:
            print ("Please pay the bill")
            print ("Your total bill is $", total_bill)
            print ("Your reamining budget is $", budget)
            if budget > 0:
                print ("Thank you for paying the bill")
                print ("Congratulations, You have earned a second date!!!")
            else:
                print ("You just lost your date")
            break


order_item(menu,budget)