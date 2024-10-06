def rev(input):
    rev = ""
    a = -1
    for i in input:
        rev = rev + input[a]
        a = a - 1
    print(f"reversed string is: {rev}")

user_str =  input("Enter a string")
rev(user_str)


