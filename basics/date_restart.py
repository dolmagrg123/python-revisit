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
    global total_bill, points
    total_bill = 0
    name_date = input("Who is on a date with you?")
    while True:
        try:
            budget = int(input("What is your budget for the date?"))
            break
        except:
            print("Please try again")

    points = 0
    print(menu)
    print ("--------------------------------------\n")
    order_self(budget,total_bill,points)



    
def order_self(budget,bill,points):

    while True:
        response = input("Would you like to order for yourself? (Y/y to order, anything else to not order): ")
        if response == "Y" or response == 'y':
            points = points - 1
            order = input("What can I get for you?")
            if order in menu:
                budget = budget - int(menu[order]["Price"])
                bill = bill + int(menu[order]["Price"])
                print("Your remaining budget is: ", budget)
                print ("--------------------------------------\n")
            else:
                points = points - 1
                print("We dont serve the food")
        else:
            print("You dont want to order")
            points = points + 1
            print("Your remaining budget is: ", budget)
            print ("--------------------------------------\n")
            order_date(budget,bill,points)
            break


def order_date(budget,total_bill,points):

    while True:
        response = input("Would you like to order for your date? (Y/y to order, anything else to not order): ")
        if response == "Y" or response == 'y':
            points = points + 3
            order = input("What can I get for your date?")
            if order in menu:
                budget = budget - int(menu[order]["Price"])
                total_bill = total_bill + int(menu[order]["Price"])
                print("Your remaining budget is: ", budget)
                print ("--------------------------------------\n")
            else:
                points = points - 1
                print("We dont serve the food")
        else:
            print("You dont want to order")
            print("Your remaining budget is: ", budget)
            print ("--------------------------------------\n")
            points = points - 1
            pay_bill(total_bill,points,budget)
            break

def pay_bill(bill,points,budget):
    print("Your total bill is:", bill)
    print ("--------------------------------------\n")
    response = input("Would you like to pay the full bill?(Y/N)")
    if response == "Y" or response == 'y':
        if budget < 0:
            print("Your bill is higer than your budget.")
            choice = input("Are you sure you want to pay?(Y/N)")
            if choice == "Y" or choice == 'y':
                points = points + 2
                print("Thank You for paying the bill") 
            else:
                print("Your date paid the bill")
    else:
        points = points - 1
        print("Your date paid the bill")
    redate(points)

def redate(points):
    if points > 2:
        print ("--------------------------------------\n")
        print("Congratulations!!, You have earned a second date!!!")
        print ("--------------------------------------\n")
    else:
        print ("--------------------------------------\n")
        print("Sorry, You did not get a second date!!!")
        print ("--------------------------------------\n")
                   

date()

