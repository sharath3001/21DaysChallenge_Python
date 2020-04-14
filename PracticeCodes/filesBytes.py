data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 - i
for b in data:
    print(hex(b))
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i
try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))
data = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))
