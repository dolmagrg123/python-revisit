# Activity:  Design a personalized menu using nested dictionaries in Python. 
# Your menu should feature different categories, such as appetizers (apps), main courses, desserts, and beverages.
# For each item in your menu, include details like price, ingredients, and any other relevant information you think would be helpful.

menu = {

    "Wings":{
        "Course":"Appetizer",
        "Ingredients" : ["Chicken", "Garlic", "BBQ Sauce"],
        "Price": 15,
        "Description": "This is the best wings in the World"
    },
    "Steak and Eggs":{
        "Course":"Main",
        "Ingredients" : ["Steak","Eggs","Salt","Pepper"],
        "Price": 45,
        "Description": "4 oz Wagyu Beef with Eggs"
    },
    "Sushirito":{
        "Course":"Main",
        "Ingredients" : ["Salmon","Mayo","Rice","Nori","Beans"],
        "Price": 25,
        "Description": "Fusion of japanese sushi with burrito"        
    },
    "Kakigori":{
        "Course":"Dessert",
        "Ingredients" : ["Shaved Ice","Matcha","Condensed Milk","Read Bean","Syrup"],
        "Price": 10,
        "Description": "Shaved ice with condensed milk for refreshing summer feels"        
    }


}

print(menu["Kakigori"]["Ingredients"][0])
