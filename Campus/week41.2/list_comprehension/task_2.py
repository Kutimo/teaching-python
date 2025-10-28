words: list[str] = ["elephant", "giraffe", "hippopotamus", "cat"]

shortened: list[str] = [word[:3:2] for word in words]

print(shortened)
