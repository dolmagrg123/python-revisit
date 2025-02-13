# Write a program to check if a number is even or odd.
# Check if a year is a leap year.

def even_odd(user_input):
    if user_input%2 == 0:
        print ("even")
    else:
        print("odd")

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("leap year")
    else:
        print("not a leap year")


user_input = int(input("Enter a number"))
even_odd(user_input)

year = int(input("Enter a year"))
leap_year(year)