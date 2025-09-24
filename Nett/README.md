# online classroom

## plan for dagen:

1. Error Handling (Exceptions in Python)
   🔹 What are errors?
2. While loops
3. while True
4. Break & Continue

# Teaching Guide: Error Handling and `break` in Python

## 1. Error Handling in Python

### What is Error Handling?

- Errors happen when something goes wrong in a program.
- Instead of crashing, we can **handle** them using `try` and `except`.

### Basic Syntax

```python
try:
    # code that might cause an error
    x = int("hello")
except ValueError:
    print("Oops! That wasn't a number.")
```

ValueError – wrong value type

ZeroDivisionError – dividing by zero

FileNotFoundError – file doesn’t exist

TypeError – wrong data type used

https://docs.python.org/3/tutorial/errors.html

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print("You entered:", num)
finally:
    print("This always runs.")
```

while loop

-Who remember the while loop?

-while loop is a loop that will run until the condition is true.

hva man kan bruke det til, fks login, nettverksøk og andre terminal prosseser.

-this while True will run forever

```python
while True:
    print("Count is:", count)
    count += 1
```

Break:

```python
while True:
    name = input("Enter your name (type 'stop' to quit): ")
    if name == "stop":
        print("Loop ended.")
        break
    print("Hello", name)
```

Analogy

-Break = walking out of the classroom.

-Continue = skipping one student’s turn, but class continues.

# Continue

# this continue skips 3 in the loop

```python
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)
```

```python
data = ["42", "100", "hello", "55"]
print(data)
for item in data:
    if not item.isdigit():
        continue   # skip invalid numbers
    print("Valid number:", int(item))
```

# finally we are going to connect everything we talked about

```python
while True:
    try:
        num = int(input("Enter a number (0 to stop): "))
    except ValueError:
        print("Invalid input, try again.")
        continue
    if num == 0:
        break
    print("You entered:", num)
```

```python
while True:
-------
    ****
    try:
        num = int(input("Skriv inn ett tall (Skriv 0 for å stoppe programmet): "))
    except ValueError:
        print("Input er ikke et tall, prøv igjen!")
        continue
    ***
    ****
    if num == 0:
        break
    ***
    ***
    print("Du skrev inn tallet: ", num)
    ***
------

```
