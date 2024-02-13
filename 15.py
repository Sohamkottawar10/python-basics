# Python program to demonstrate the use of update() method
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)
print("Set1 : ", set1)
print("Set2 : ", set2)
# Update method
set1.update(set2) # it will add elements to the set1 from set2
print("Updated Set1 : ", set1)
# Print the updated set
# print(set1)
# List is passed as an parameter which gets automatically converted to a set

set1.update(list3)
print("Updated Set1 : ", set1)
print(set1)