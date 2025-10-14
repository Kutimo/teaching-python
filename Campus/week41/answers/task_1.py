# Filter names that start with a vowel

names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Tom"]

vowels = ["a", "e", "i", "o", "u"]


# Using list comprehension with .startswith()

# filtered_names = [
#     name for name in names if name.lower().startswith(tuple(vowels))]

# print(filtered_names)

filtered_names = [name for name in names if name[0].lower() in vowels]

print(filtered_names)
