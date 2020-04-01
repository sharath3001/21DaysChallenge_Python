# Copying the whole list
list1 = [1]
list2 = list1[:] #slice else both lists will have same memory location
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[-2:-1] # negative index with slices
print(newList)

myList = [10, 8, 6, 4, 2]
newList = myList[:3] # default start is index 0 and same goes with end
print(newList)

myList = [10, 8, 6, 4, 2]
del myList[1:3] # deleting using slice
print(myList)

# in and not in operators
myList = [0, 3, 12, 8, 2]
print(5 in myList)
print(5 not in myList)
print(12 in myList)

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2
del l1[0]
del l2
print(l3)
