Key skills for Week 38:

Know how to create, add/remove items, loop, and access each type.

Understand when to use which:

List = order matters, can have duplicates.

Tuple = fixed data.

Set = no duplicates, fast membership test.

Dict = fast lookups by name/ID.

### Lists

Ordered collection (keeps the order you insert things).

Can change after creation (mutable).

Great for storing a bunch of items you want to loop through.

```python
books: list[str] = ["1984", "Brave New World", "The Hobbit"]

# Add a book
books.append("Dune")

# Access by index
print(books[0])   # "1984"

# Change a book
books[2] = "Lord of the Rings"

# Loop through list
for book in books:
    print(book)

# Remove a book
books.remove("1984")
```

### Tuples

Ordered collection (keeps the order you insert things).

Cannot change after creation (immutable). (This means in runtime)

Like lists, but cannot be changed (immutable).

Useful for fixed collections (e.g., coordinates).

```python
point: tuple[int, int] = (10, 20)
print("Point:", point)
point[0] = 30  # This will throw an error  # This will throw an error
```

### Sets:

Unordered, no duplicates.

Useful when you only care if something exists, not the order.

```python
unique_numbers: set[int] = {1, 2, 3, 3, 4}
unique_numbers.add(5)
print("Unique numbers:", unique_numbers)

if 3 in unique_numbers:
    print("3 is in the set")
```

### Dictionaries(dict):

Key → Value storage.
Great when you need to look up something by a name/ID.

```python
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

del person["hobby"]

print("Person dictionary:", person)

```

This can be handy with large api calls or data sets or very complex data structures.

```python
from typing import Any

person: dict[any] = {
    "name": "Oliver",
    "age": 29,
    "is_programmer": True
}
print(person)
```

Key skills for Week 39:

Write your own functions.

Use parameters + return values.

Know when to reuse instead of rewriting code.

Understand scope.

## Functions :

### Defining and calling functions

```python
def say_hello():
  print("Hello")

say_hello()
```

### Return values:

```python
def add(a:int, b:int) -> int:
    return a + b

result = add(5, 3)
print(result)   # 8
```

### Parameters and return values

```python
def greet(name: str ="world") -> str:
    print(f"Hello, {name}!")

greet()
greet("Oliver")

```

```python
def total_price(price: int, quantity: int) -> int:   # price and quantity are PARAMETERS
    return price * quantity


print(total_price(10, 5))  # 10 and 5 are ARGUMENTS
```

### Functions + data structures

```Python
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

scores: list[float] = [90.0, 80.0, 100.0]  # notice the .0
print(average(scores))   # 90.0

```

### Scope (local vs global)

```python
x:str = 10  # global

def test() -> None:
    x = 5  # local
    print(x)

test()     # 5
print(x)   # 10

```

### Functions Calling Functions

-Functions can be combined to build more complex logic:

```python
def add(a:int, b:int) -> int:
    return a + b

def multiply(a:int, b:int) -> int:
    return a * b

def calculate(a: int, b: int) -> int:
    return multiply(a, b) + (a + b)

print(calculate(2, 3))  # (2+3) * (2*3) = 5 * 6 = 30
```
