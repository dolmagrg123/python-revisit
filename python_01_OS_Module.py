import os

def count_items():
    dir = input("Enter the path of directory do you want to count the number of items?")

    no_of_file = 0
    no_of_dir = 0
    try:
        # use os.listdir(dir) function to return list of files and directory present
        directory = os.listdir(dir)

        for item in directory:
            # used os.path.join to add the item in the complete path
            # os.path.isfile to check if an item is file or directory
            if os.path.isfile(os.path.join(dir, item)) :
                no_of_file +=1
            else:
                no_of_dir +=1
        print("Number of file = ", no_of_file)
        print("Number of dir = ", no_of_dir)
    except FileNotFoundError:
        print(f"{dir} does not exist")
        count_items()
    

count_items()