squares = [x**2 for x in range(10)]
print(squares)


squares_generator = (x**2 for x in range(10))
print(list(squares_generator))
