def squares(start, end):
	squares = [value ** 2 for value in range(start, end + 1)]
	return squares

print(squares(2, 3))
print(squares(1, 5))
print(squares(0, 10))