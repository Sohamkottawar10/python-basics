# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Apple'
Dict[1] = 'Banana'
Dict[2] = 'Mango'
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values to a single Key
Dict[3] = 'Orange', 'Cherry', 'Guava'
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Water Mellon'
print("\nUpdated key value: ")
print(Dict)
Dict[4] = 'pineapple'
print(Dict)

# Delete using value.
del(Dict[3])
print(Dict)
#using value : values in a dictionary are not guaranteed to be unique, so this method will only remove the first matching value found.
idx=0
for i in Dict:     #dont use for i in range(len(Dict)) since the index are not consecutive
    if Dict[i] == 'Banana':
        idx=i
if idx != 0:
    del(Dict[idx])
print(Dict)
# value_to_delete = 'Banana'
# delete_element_by_value(Dict,value_to_delete)
# print(Dict)