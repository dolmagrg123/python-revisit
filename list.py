# Write a function to remove duplicates from a list.


thislist = ["apple", "banana", "cherry", "apple", "cherry"]

def remove_duplicates(thislist):

    newlst =[]

    for x in thislist:
        if x not in newlst:
            newlst.append(x)
    return newlst

#alternate method
def duplicate_set(thislist):
    return list(set(thislist))