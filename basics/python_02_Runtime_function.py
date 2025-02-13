'''
Write a Python function that calculates the uptime percentage of a service based on the total number of hours and the number of hours the service was down. 
The function should take 2 parameters(total hours and down hours, inputted when the function is run). 
Lastly, the function should return the uptime percentage rounded to two decimal places. 
'''

def uptime(total_hours,down_hours):

    uptime = total_hours - down_hours
    up_percent = round(((uptime/total_hours) * 100),2)
    return up_percent


total_hours = float(input("Enter the total number of hours: "))
down_hours = float(input("Enter the number of hours service was down: "))
up = uptime(total_hours,down_hours)
print(f"The uptime percentage is {up}")

