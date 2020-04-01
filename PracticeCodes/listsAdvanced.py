squares = [x ** 2 for x in range(10)] # list comprehension
print(squares)

board = [[i for i in range(8)] for j in range(8)]# two dimensional (matrix)
print(board)

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)] # three dimensional
print(rooms)
