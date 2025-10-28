names: list[str] = ["Alice", "bob", "eve", "Oscar", "Uma", "Tom"]

vowels: list[str] = ["a", "e", "i", "o", "u"]

# filtered_names: list[str] = [
#     name for name in names if name[0].lower() in vowels]

filtered_names: list[str] = [
    name for name in names if name.startswith(tuple(vowels))]


print(filtered_names)
