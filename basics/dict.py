
# Implement a function that takes a string and returns a dictionary of character frequencies.


new_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''


def freq(new_string):
    new_dict = {}

    for char in new_string.lower() :
        if char == " " or char == "\n":
            continue
        if char not in new_dict.keys():
            new_dict[char] = 1
        else:
            new_dict[char] += 1
    print(new_dict)



freq(new_string)

#alternate method:
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

    