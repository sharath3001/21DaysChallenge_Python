myTuple = (1, 10, 100, 1000) # immutable and can also tak values without parenthesis
myTuple1 = () # empty tuple
myTuple2 = (2,) # single element , is compulsory for 2, also
print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])
for elem in myTuple:
    print(elem)

myTuple = (1, 10, 100)
t1 = myTuple + (1000, 10000)
t2 = myTuple * 3
print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)
print(myTuple)

# count() method is used to count no of particular element in a tuple
# dictionary
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']
print(dict)
print(dict['dog']) # get() method can also be used
for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")

dict = {"dog" : "chien", "cat" : "chat", "horse" : "cheval"}
for key in dict.keys(): # keys() method returns a list of all keys
    print(key, "->", dict[key])
for key in sorted(dict.keys()): # sorted function returns a sorted list
    print(key, "->", dict[key])
for english, french in dict.items(): # items method returns tuples where each tuple is a key value pair
    print(english, "->", french)
for french in dict.values(): # values() method returns a list of all values
    print(french)
dict['cat'] = 'minou'
dict['swan'] = 'cygne'
dict.update({"duck" : "canard"})
del dict['dog'] # clear() method removes all items
dict.popitem() # deletes last item of dictionary

# tuple can be converted to list using list() and vice versa using tuple() and tuple can be converted to dictionary using dict()
# copy() method is used to copy a dictionary
