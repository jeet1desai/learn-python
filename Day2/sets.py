number_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9 ]
print(set(number_list))
print(type(set(number_list)))

# Print
number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for item in number_set:
    print(item)

# Add
number_set.add(10)
print(number_set)

# Remove
number_set.remove(3)
print(number_set)