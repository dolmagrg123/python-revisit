
def palindrome(w): 
    length = len(w)

    for i in range(length//2):
        if w[i] != w[length -i -1]:
            return False
    return True
    


word = input("Enter a string: ")
if palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")