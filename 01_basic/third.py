l = [1, 2, 3, 4, 5]
# l.insert(3, 1) # Insert(location, element)
# l.remove(1) # Remove the first occurence
# l.remove(1)
# l.insert(0, 1)
# # l.pop()
# l.sort(reverse=True)
l.reverse()
# print(l)

s = [1,4,5,2,3,5]
s.reverse()
# print(s)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7, 8}
# set1.update(set2)
# set1.remove(10) # Throw error if not exist
# set1.discard(19)
# print(set1)

# print(f"Union : {set1.union(set2)}")
# print(f"Difference : {set1.difference(set2)}")
# print(f"Intersection : {set1.intersection(set2)}")
# print(f"Symmetric Difference : {set1.symmetric_difference(set2)}")


list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[::2])