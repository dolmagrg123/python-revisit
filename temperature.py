def fahrenheit_to_celcius(degree):

    temp= (37/98.6) * degree
    print(f"{degree} Fahrenheit is {temp} Celcius")


temp = float(input("Enter a temperature in Fahrenheit: "))
fahrenheit_to_celcius(temp)