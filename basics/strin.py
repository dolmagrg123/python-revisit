#Create a list of 5 numbers and print the sum
# a = "12345"

# b = int(a)

# print(type(b))
# print(type(a))

# total_length = "Hello, World!"

# print (len(total_length))

list_num = [3,34,2,1,55]
# sum = 0
# for x in list_num:
#     sum = sum + x


# print(sum)
#Reverse a list without using .reverse().
list_two = []

count = len(list_num)
# print(count)

try:
    for x in range(count):
        list_two.append(list_num[count])
        count = count -1
    print(list_two)
except Exception as e:
    print(str(e))
    for x in range(count):
        list_two.append(list_num[count-1])
        count = count -1
    print(list_two)
    
    


