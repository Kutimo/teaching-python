## Overview

- Recap loop and lists
- Recap functions and Modules(import)
- What list comprehensions are and how they work
- Recap functions and modules
- How to use lambda (anonymous) functions
- When to use them together
- Real-world examples and exercises

#### Functions and modules

- Functions
- Modules (import)

#### Loops and lists

- For loops
- Simple functions
- Basic list operations (`append`, `range`, etc.)

Example:

```python
names: list[str] = ["alice", "bob", "carol"]
upper_names: list[str] = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)
```

Q: Can this be written shorter?

##### List comprehensions

- List comprehensions = readable, concise looping
- Replace for loops with list comprehensions

##### Syntax:

```python
[expression for item in iterable if condition]
```

How it works:

- `expression`: what to do with each item
- `for item in iterable`: where the data comes from
- `if condition`: (optional) filter condition

examples:

```python
# Squares of numbers
squares: list[int] = [n * n for n in range(6)]

# Even numbers only
evens: list[int] = [n for n in range(10) if n % 2 == 0]

# Uppercase names
names: list[str] = ["alice", "bob", "carol"]
upper_names: list[str] = [name.upper() for name in names]
```

**Shorter is not always better!**

#### Comparison

**Without comprehension:**

```python
result: list[int] = []
for n in range(10):
    if n % 2 == 0:
        result.append(n)
```

**With comprehension:**

```python
result: list[int] = [n for n in range(10) if n % 2 == 0]
```

- This is cleaner, shorter and faster.

#### Nested Comprehension

Here we have a list of lists
and we want to make 1 list instead, also called flattening the list

```python
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
flattened: list[int] = [num for row in matrix for num in row]
```

First we go through the first list and iterate over the numbers, then again for the second list.

#### Exercise

1: Filter names that start with a vowel

```python
names: list[str] = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Tom"]

vowels: list[str] = ["a", "e", "i", "o", "u"]

# hint:
# use .startswith()
# Or index
```

expected output:

```bash
 ['Alice', 'Eve', 'Tom']
```

2: Shorten words to their first 3 letters

```python
words:list[str] = ["elephant", "giraffe", "hippopotamus", "cat"]

# Hint use slicing
```

expected output:

```bash
 ['ele', 'gir', 'hip', 'cat']
```

| Pros                                         | Cons                                         |
| -------------------------------------------- | -------------------------------------------- |
| Shorter and cleaner than regular `for` loops | Hard to read when too complex or nested      |
| Easy to read when simple                     | Not good for side effects (like `print`)     |
| Usually faster than normal loops             | Difficult to debug or add breakpoints inside |
| Can include filters using `if`               | Can use more memory for very large lists     |
| "Pythonic" and expressive                    | —                                            |

#### Recap functions and modules

#### functions

- Simple functions
- Parameters and return values
- return types and type hints are recommended

```python
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))
```

```python
def is_even(n: int) -> bool:
    return n % 2 == 0


print(is_even(3))  # False
print(is_even(4))  # True
```

#### arguments and parameters

What is a parameter?
and what is and argument?

#### Default parameters

```python
def log_message(message: str, level: str = "info") -> str:
    return f"[{level}] {message}"

print(log_message("System started"))             # Output: [INFO] System started
print(log_message("Disk almost full", "WARN"))  # Output: [WARN] Disk almost full
```

#### Modules

-Keep your code organized

-Avoid rewriting the same functions

-Use prebuilt functionality (like math)

-Makes it easier to collaborate with others

#### Built in modules

```python
import math

# Use sqrt() to calculate square root
print(math.sqrt(16))  # Output: 4.0

# Use pi constant
print(math.pi)        # Output: 3.141592653589793

# Use factorial()
print(math.factorial(5))  # Output: 120
```

#### Selfmade modules

```python
#main.py
import module

print(module.double_list([111, 2, 3]))  # Output: [2, 4, 6]

# module.py
def double_list(numbers: list[int]) -> list[int]:
    return [n*2 for n in numbers]

```

These 2 files are in the same folder

Example 2:

```python
#main.py

from lib.string_utils import capitalize_words

text = "hello world from python"
result = capitalize_words(text)
print(result)  # Output: Hello World From Python

# lib/string_utils.py
def capitalize_words(input_str: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.

    :param sentence: string to capitalize
    :return: capitalized string
    """
    return " ".join([word.capitalize() for word in input_str.split()])

```

#### Lambda functions

- Anonymous functions
- Short and compact
- Used for short tasks

```

```

```

```

```
