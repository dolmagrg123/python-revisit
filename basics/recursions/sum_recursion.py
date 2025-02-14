def sum_recursion(n):
    if n == 0 :
        return 0
    last_digit = n % 10
    # print(last_digit)
    return last_digit + sum_recursion(n//10)

print(sum_recursion(123))