import time
for i in range(1,6): # i is counter variable
    print(i,"Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# break and continue are available as per other languages

while 1:
    if input() == "chupacabra":
        break
print("You've successfully left the loop.")

# ugly vowel eater
wordWithoutVovels = ""
userWord = input("Enter any word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue  
    else:
        wordWithoutVovels += letter

print(wordWithoutVovels)

c0 = int(input("Number: "))

# collatz's hypothesis
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        print(c0)
        steps += 1
    else:
        c0 = int(c0 * 3 + 1)
        print(c0)
        steps += 1
print("steps",steps)

