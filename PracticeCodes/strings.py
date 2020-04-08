word = 'by'
print(len(word))
empty = ''
print(len(empty))
i_am = 'I\'m'
print(len(i_am))
multiLine = '''Line #1
Line #2'''
print(len(multiLine))
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
ch1 = 'a' # only one character is permitted
ch2 = ' ' # space
print(ord(ch1)) # ordinal function returns code point
print(ord(ch2))
print(chr(97)) # opposite of above function 
print(chr(945))
exampleString = 'silly walks'
for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')
print()
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" in alphabet)
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
print(list("abcabc"))
print("abcabc".count("b"))
print('abcabc'.count("d"))
