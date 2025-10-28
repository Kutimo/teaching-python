names: list[str] = ["John", "bob", "caRol", "Alice"]

sorted_names: list[str] = sorted(names, key=lambda x: x.lower())

print(names)
print(sorted_names)

print(sorted(names))
