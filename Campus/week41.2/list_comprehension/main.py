
# Kvadrat av tall

# squares: list[int] = [n * n for n in range(6)]

# print(squares)


# Tall partall

# evens: list[int] = [n for n in range(1, 10) if n % 2 == 0]
# print(evens)

# Store bokstaver
# names: list[str] = ["alice", "bob", "carol"]

# upper_names: list[str] = [name.upper() for name in names]

# print(upper_names)


# Nested comprehension

matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]

flattened: list[int] = [num for row in matrix for num in row]
print(flattened)
