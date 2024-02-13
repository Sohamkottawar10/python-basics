def intersection(list1, list2):
    return list(set(list1) & set(list2))


List1 = [1, 2, 3, 4]
List2 = [1, 4, 2, 3, 5]
print("List1 : ", List1)
# List3 = List1 #by doing this List3 will point to same memory location of List1
List3 = List1.copy()
print("Intersection : ", intersection(List1,List2))
# print("List1 : ", List1)
for i in range(len(List2)):
    if not List2[i] in List1:
        List3.append(List2[i])
        #or for union do : 

print("List2 : ", List2)
print("Intersection : ", intersection(List1,List2))
print("Union : ", List3)
#print("Intersection : ", intersection(List1,List2)) 




