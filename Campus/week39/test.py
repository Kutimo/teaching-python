person: dict[str | int | bool] = {
    "name": "Oliver",
    "age": 29,
    "is_programmer": True
}
person["hobby"] = "coding"
person["programming_languages"] = ["c#", "python", "java"]

print("Person dictionary:", person)

for key, value in person.items():
    print(f"{key}: {value}")

del person["hobby"]  # Delete keyword, frees up memory space at runtime

print("Person dictionary:", person)
