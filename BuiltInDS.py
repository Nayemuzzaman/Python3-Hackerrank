print("----------List-----------------")
# Lists are mutable(changeable)
# List can have heterogeneous. That's means containing different types of objects

list1 = [1, 2, 3, "nayem"]
print(list1)

# append(), extend and insert()
list1.append((2, 0))
list1.insert(3, 'example')
print(list1)

# del, pop(), remove()
del list1[3]
print("list", list1)
# pop delete by position
a = list1.pop(0)
print(a)
print(list1)
# remove delete value
list1.remove(2)
print(list1)

print(list1)
# print o to 2
print(list1[0:2])
# print 0 to 3 and skip 2 position
print(list1[0:3:2])
# print reverse order
print(list1[::-1])

print("----------List sort-----------------")
list2 = [1, 2, 4, 5, 6, 90, 40]
print(sorted(list2))
list2.sort(reverse=True)
print(list2)
print(list2.index(2))
print(list2.index(4))

print("----------Tuple-----------------")
# Tuple are immutable
# faster than list
tuple1 = (1, 2, 3)
print(tuple1)

tuple1 = tuple1 + (4, 5, 6)
print(tuple1)

# list value will changed but in tuple not possible , tuple shows error
list3 = [1, 2, 3]
list3[1] = 0
print(list3)

print("----------Dictionary-----------------")
dict1 = {1: "javascript", 2: "java", 3: "C", 4: "C++"}
print(dict1)
# now javascript change to python
dict1[1] = 'python'
print(dict1)
# how to add value in dictionary
dict1[5] = "Ruby"
print(dict1)
# delete(1: "javascript") value in dictionary
del dict1[1]
print(dict1)
# pop(java) in dictionary
print(dict1.pop(2))
print(dict1)
# in pop item last one will pop
print(dict1.popitem())
print(dict1)
# show all keys
print(dict1.keys())
# show all values
print(dict1.values())
# print all items in pair
print(dict1.items())

print("----------Set-----------------")
# it works for arithmetic
# un-order collection of unique elements. Its also mutable

set1 = {1,2,3,4,4,4}
# here print 1234, repeat number print only one time
print(set1)
#add value in set
set1.add(5)
print(set1)
# As like mathematic set also have union(), intersection(), difference(), symmetric_difference()
set2 = {3,4,5,6,7,8,9}
# union have print all of value, repeat value print one time
print(set1.union(set2))
# intersection print common value
print(set1.intersection(set2))
# both common will deduct and set1 uncommon will print
print(set1.difference(set2))
# both uncommon will print
print(set1.symmetric_difference(set2))
















