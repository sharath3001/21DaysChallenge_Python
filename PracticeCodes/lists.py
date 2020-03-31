numbers = [10, 5, 7, 2, 1]
print("List content:", numbers) # printing original list content
numbers[0] = 8
numbers[1] = numbers[4]
print("List content:", numbers)
print("\nList length:", len(numbers)) # printing the list's length
del numbers[1] # removing the second element from the list
print(numbers[-1])
print(numbers[-2]) # negative indices are legal and starts from last with index -1
numbers.append(4) # inserts element after the last element of list
numbers.insert(0, 222) # inserts at 0 index and all elements are shifted right

myList = [] # creating an empty list
for i in range(5):
    myList.append(i + 1)
print(myList)

# swapping two variables
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1 # same goes with list

# bubble sort
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)
# sorting can also be done using myList.sort() method
# list can be reversed using myList.reverse() method
