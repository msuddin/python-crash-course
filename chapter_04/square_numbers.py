squares = [] # start with an empty list

for value in range(1, 11): # loop starting at 1 until value is 11
    square = value ** 2 # new variable called square that has the value of value to the power of itself
    squares.append(square)

print(squares)