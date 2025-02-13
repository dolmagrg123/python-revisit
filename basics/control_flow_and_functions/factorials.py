
def factorials_num(number):
    factorial = 1
    while number >1:
        factorial = number * factorial
        number -= 1
    print(factorial)

def sum(list_a):
    sum = 0
    for x in list_a:
        sum += x
    print(sum)

# new_list = [1,2,3]
sum([1,2,3,4,5,6,7,8,9,10])
# factorials_num(10)
