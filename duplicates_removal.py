# Remove duplicates from [1, 2, 3, 3, 4, 5, 5, 6] using sets.

original_list = [1,2,3,3,4,5,5,6]

no_duplicates = list(set(original_list))

# print(no_duplicates)

# Find the intersection of {1, 2, 3} and {2, 3, 4}.
set_a = {1,2,3}
set_b = {2,3,4}

# intersection_set = set_a.intersection(set_b)

# print(intersection_set)

#alternate method
print(set_a & set_b)


#Dictionaries

# Create a dictionary with keys name, age, city.
# Add a new key country.

student = {'name': 'Dolma', 'age': 25, 'city': 'New York'}
student['country'] = 'USA'
print(student) 
