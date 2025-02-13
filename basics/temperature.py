def fahrenheit_to_celcius(degree):

    temps= (37/98.6) * degree
    print(f"{degree} Fahrenheit is {temps} Celcius")

def user_input():
    try:
        temp = float(input("Enter a temperature in Fahrenheit: "))
        return temp
    except:
        print("Incorrect value. Please try again")
        user_input()

fahrenheit_to_celcius(user_input())

