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

def date():
    # global name_date
    name_date = input("Who is on a date with you?")
    # global budget
    budget = int(input("What is your budget for the date?"))
    global total_bill
    total_bill = 0
    print(menu)
    order_self(budget,total_bill)
    order_date(budget,total_bill,name_date)
    pay_bill(total_bill)
    
def order_self(budget,total_bill):

    while True:
        response = input("Would you like to order for yourself? (Y/N)")
        if response == "Y" or response == 'y':
            order = input("What can I get for you?")
            budget = budget - int(menu[order]["Price"])
            total_bill = total_bill + int(menu[order]["Price"])
            print("Your remaining budget is: ", budget)
        else:
            print("Your current bill is: ", bill)
            return bill


# def order_date(budget,total_bill,name):

#     while True:
#         response = input("Would you like to order for your date? (Y/N)")
#         if response == "Y" or response == 'y':
#             order = input("What can I get for your date?")
#             budget = budget - int(menu[order]["Price"])
#             total_bill = total_bill + int(menu[order]["Price"])
#             print("Your remaining budget is: ", budget)
#         else:
#             break

def pay_bill(bill):
    print("Your total bill is:", bill)

date()








    




# def order_item(menu,budget):
#     total_bill = 0
#     print(menu)
#     while True:
#         response = input("Would you like to order? (Y/N)")
#         count = 0
#         if response == 'Y' or response == 'y' :
#             count = count + 1
#             food = input("What would you like to eat?")
#             budget = budget - int(menu[food]["Price"])
#             total_bill = total_bill + int(menu[food]["Price"])
#             print("You have", budget , "dollars remaining in your budget")
#         else:
#             print ("Please pay the bill")
#             print ("Your total bill is $", total_bill)
#             print ("Your reamining budget is $", budget)
#             if budget > 0:
#                 print ("Thank you for paying the bill")
#                 print ("Congratulations, You have earned a second date!!!")
#             else:
#                 print ("You just lost your date")
#             break


# order_item(menu,budget)