# 🐍 Python Lecture: List Comprehension & Lambda Functions

**Duration:** 3 hours  
**Level:** Beginner → Intermediate  
**Goal:** Learn to write cleaner, faster Python code using list comprehensions and lambda functions.

---

## 🧠 Overview

- What list comprehensions are and how they work
- How to use lambda (anonymous) functions
- When to use them together
- Real-world examples and exercises

---

## Lecture Outline

### **Part 1: Warm-up (15 min)**

> 💬 **Speaker Note:** Start by ensuring everyone remembers loops, lists, and basic functions.

#### Recap: Loops and Lists

- For loops
- Simple functions
- Basic list operations (`append`, `range`, etc.)

**Example:**

```python
names = ["alice", "bob", "carol"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)
```

➡️ Question: Can this be written shorter?

---

### **Part 2: List Comprehension (60 min)**

> 💬 **Speaker Note:** Explain that list comprehensions replace loops for building lists.  
> Demonstrate syntax and build from simple to complex examples.

#### 🧩 Syntax

```python
[expression for item in iterable if condition]
```

**Parts:**

- `expression`: what to do with each item
- `for item in iterable`: where the data comes from
- `if condition`: (optional) filter condition

---

#### 💡 Simple Examples

```python
# Squares of numbers
squares = [n * n for n in range(6)]

# Even numbers only
evens = [n for n in range(10) if n % 2 == 0]

# Uppercase names
names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
```

> 💬 **Speaker Note:** Emphasize readability — shorter doesn't always mean better unless it’s clear.

---

#### 🧠 Comparison

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

✅ Cleaner, shorter, and faster.

---

#### ⚙️ Nested Comprehensions

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
```

> 💬 **Speaker Note:** Explain it step-by-step — “for each row in matrix, for each num in row”.

---

#### 🧩 Exercises

1. Create a list of tuples `(number, square)` for numbers 1–10:

   ```python
   [(n, n**2) for n in range(1, 11)]
   ```

2. Extract all vowels from a sentence.
3. Build a 5x5 grid of coordinates:
   ```python
   [(x, y) for x in range(5) for y in range(5)]
   ```

---

### **☕ Break (10 min)**

> 💬 **Speaker Note:** Encourage students to try rewriting some of their own loops using comprehensions during break.

---

### **Part 3: Lambda Functions (60 min)**

> 💬 **Speaker Note:** Introduce lambda as “anonymous functions” — functions without a name.

#### 🧩 Syntax

```python
lambda arguments: expression
```

**Example:**

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

---

#### 💡 Normal vs Lambda

**Normal function:**

```python
def square(x):
    return x * x
```

**Lambda:**

```python
square = lambda x: x * x
```

> 💬 **Speaker Note:** Same functionality, but lambda is inline and compact.

---

#### ⚙️ Common Use Cases

**With `map()`:**

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
```

**With `filter()`:**

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
```

**With `sorted()`:**

```python
names = ["bob", "Alice", "carol"]
sorted_names = sorted(names, key=lambda x: x.lower())
```

---

#### 🧠 Exercises

1. Filter out words shorter than 5 letters.
2. Sort a list of tuples by the second element.
3. Combine `map()` and `lambda` to uppercase names and add a suffix.

> 💬 **Speaker Note:** Encourage experimenting — lambdas are most powerful in combination with higher-order functions.

---

#### ⚔️ Discussion

**Pros:**

- Compact syntax
- Great for short, one-time use

**Cons:**

- Hard to debug or read when overused

**Rule of thumb:**

> Use `lambda` for simple, inline logic.  
> Use `def` for anything complex.

---

### **Part 4: Combining List Comprehension + Lambda (20 min)**

> 💬 **Speaker Note:** Show how both tools can work together.

#### Example 1:

```python
nums = [1, 2, 3, 4, 5]
squares = [(lambda x: x**2)(n) for n in nums]
```

#### Example 2:

```python
data = ["apple", "banana", "pear", "kiwi"]
result = [len(fruit) for fruit in data if (lambda x: "a" in x)(fruit)]
```

---

#### 🧩 Group Exercise

Given:

```python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Eve", "age": 30}
]
```

✅ Task: Extract all names where `age > 18`

**Solution:**

```python
adults = [u["name"] for u in users if (lambda x: x > 18)(u["age"])]
print(adults)
```

> 💬 **Speaker Note:** Walk through the logic slowly, explaining lambda’s role inside the comprehension.

---

### **Part 5: Wrap-up & Q&A (15 min)**

#### Recap

- List comprehensions make loops shorter and cleaner.
- Lambdas make inline logic compact.
- Both improve code readability (when used wisely).

---

#### Quick Quiz

1. What’s the main difference between `lambda` and `def`?
2. When should you use a list comprehension instead of a loop?
3. What does this return?
   ```python
   [x for x in range(5) if x % 2]
   ```

---

### **Homework / Practice**

1. Recreate simple versions of `map()`, `filter()`, and `reduce()` using list comprehensions.
2. Use both list comprehensions and lambdas to process CSV data (like filtering rows).
3. Write a function that:
   - Takes a list of strings
   - Filters words that contain `"e"`
   - Returns their lengths (all in one line)

---

## ✅ Key Takeaways

- List comprehensions = readable, concise looping
- Lambdas = short anonymous functions
- Use both to make your Python code **elegant and efficient**
