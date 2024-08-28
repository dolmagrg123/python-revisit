addition = 25

def sum(a,b):
    global addition
    print ("inside function", addition)
    addition = a+ b
    # print(addition)
    print("The sum of a and b is: ", addition,"inside function")

print ("first value", addition)

sum(2,3)
print ("global value outside function addition is", addition)
addition =3
print ("third time", addition)