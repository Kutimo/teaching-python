## Overview

- Recap loop and lists
- Recap functions and Modules(import)
- What list comprehensions are and how they work
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
names = ["alice", "bob", "carol"]
upper_names = []

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
squares = [n * n for n in range(6)]

# Even numbers only
evens = [n for n in range(10) if n % 2 == 0]

# Uppercase names
names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
```

**Shorter is not always better!**

#### Comparison

**Without comprehension:**

```python
result = []
for n in range(10):
    if n % 2 == 0:
        result.append(n)
```

**With comprehension:**

```python
result = [n for n in range(10) if n % 2 == 0]
```

- This is cleaner, shorter and faster.

#### Nested Comprehension

Here we have a list of lists
and we want to make 1 list instead, also called flattening the list

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
```

First we go through the first list and iterate over the numbers, then again for the second list.

#### Exercise

1: Filter names that start with a vowel

```python
names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Tom"]

vowels = ["a", "e", "i", "o", "u"]

# hint:
# use .startswith()
```

expected output:

```bash
 ['Alice', 'Eve', 'Tom']
```

2: Shorten words to their first 3 letters

```python
words = ["elephant", "giraffe", "hippopotamus", "cat"]
# Hint use slicing word[:3]
```

expected output:

```bash
 ['ele', 'gir', 'hip', 'cat']
```

- Pros and cons

#### Lambda functions

```

```

```

```
