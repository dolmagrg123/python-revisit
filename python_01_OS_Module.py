import os

dir = input("Enter the path of directory do you want to count the number of items?")

no_of_file = 0
no_of_dir = 0

directory = os.listdir(dir)
# print(directory)

for item in directory:
    if os.path.isfile(os.path.join(dir, item)) :
        no_of_file +=1
    else:
        no_of_dir +=1
print("Number of file = ", no_of_file)
print("Number of dir = ", no_of_dir)