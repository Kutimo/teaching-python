# campus

## plan for dagen:

1. While loops
2. while True
3. Break & Continue
4. Practice problems
5. Lists introduction
6. Wrap-up

1- while loop

-Who remember the while loop?

-while loop is a loop that will run until the condition is true.

```python
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1
```

-this while True will run forever

```python
while True:
    print("Count is:", count)
    count += 1
```

```python
while True:
    name = input("Enter your name (type 'stop' to quit): ")
    if name == "stop":
        print("Loop ended.")
        break
    print("Hello", name)
```

## hva er break?

## hva er continue?

Analogy

-Break = walking out of the classroom.

-Continue = skipping one student’s turn, but class continues.

```python
while True:
    text = input("Type 'stop' to quit: ")
    if text == "stop":
        print("Loop ended.")
        break
    print("You typed:", text)
```

```python
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)
```

#oppgave 1

# oppgave 2

```python
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
```

# oppgave 3

Skriv et program som ber brukeren om passord "Gokstad123".

```bash
Enter password: hello
Wrong, try again!
Enter password: python123
Access granted!
```

3- some assignments and activities are in the course Moodle page.

- Jobbe oss igjenom et par oppgaver fra Aktiviteter.py

4- list

-What is a list?

-List is a sequence of items.

-List is mutable.

-List is ordered.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[1])   # banana

for fruit in fruits:
    print("I like", fruit)

fruits.append("orange")
print(fruits)
```

```python

movies = ["Inception", "Matrix", "Titanic"]

for movie in movies:
    print(movie)

movies.append("Avatar")
print(movies)

```

most of students got the while loop and break and continue. but some of them struggling with "while True" and also "continue". if you could focus on that, it would be amazing.
