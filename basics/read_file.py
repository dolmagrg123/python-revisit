a = open("data.txt")
line_num = 1
for line in a:
    print(line_num, line)
    line_num += 1