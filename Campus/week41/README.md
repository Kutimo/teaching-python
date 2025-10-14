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






- Pros and cons

#### Lambda functions
