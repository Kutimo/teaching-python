Key skills for Week 39:

Write your own functions.

Use parameters + return values.

Know when to reuse instead of rewriting code.

Understand scope.

## Functions :

### Functions Calling Functions

-Functions can be combined to build more complex logic:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b):
    return add(a, b) * multiply(a, b)

print(calculate(2, 3))  # (2+3) * (2*3) = 5 * 6 = 30
```
