name = "Wanda"
# print(name)

second_name = "Bruce"

# print(name + " " +  second_name)
# print(name , second_name)

weight = 300
# print(weight)
# if we combine strings, we can use + to add strings
# but use comma(,) to add strings with integers(different data types)

print( "My name is " , second_name, "and my weight is", weight)

weight_string = "300"
print( "My name is " + second_name + " and my weight is " + weight_string)

weight_gained = "20"

total_weight =int(weight_string) +int(weight_gained)
print("total weight is: " ,total_weight)

height = "6'3"
# print(height)

blood_pressure = "120/80"
# print(blood_pressure)

print(type(blood_pressure))

temperature = 98.5
print(temperature)
print(type(temperature))

temperature = int(96.3)
print("New Temperature is: ", temperature)
print(type(temperature))

temperature = 3
print("Final temperature is: " , temperature)

superPowers = ["Flying", "Strength", "Wisdom"]
print(superPowers)
print(type(superPowers))
print(len(superPowers))

super_powers = ("Flying", "Strength", "Wisdom")
print(type(super_powers))

print(f"My name is {name} and I weigh {weight} pounds.")

print("Hello, stranger.",name)