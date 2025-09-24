import math

# 1. Enkel hilsen


def hello_world() -> None:
    print("Hei, verden!")

# 2. Personlig hilsen


def greet(name: str) -> None:
    print(f"Hei, {name}!")

# 3. Legg sammen to tall


def add_numbers(a: float, b: float) -> None:
    print(a + b)

# 4. Multipliser to tall og returner resultatet


def multiply(a: float, b: float) -> float:
    return a * b

# 5. Sjekk om partall


def is_even(number: int) -> bool:
    return number % 2 == 0

# 6. Sirkelens omkrets


def circle_circumference(radius: float) -> float:
    return 2 * math.pi * radius

# 7. Sjekk om to strenger er like


def strings_equal(str1: str, str2: str) -> bool:
    return str1 == str2

# 8. Sekunder til timer og minutter


def seconds_to_hours_minutes(seconds: int) -> tuple[int, int]:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes

# 9. Tell antall ord i en setning


def count_words(sentence: str) -> int:
    words = sentence.split()
    return len(words)

# 10. Finn største av tre tall


def max_of_three(a: float, b: float, c: float) -> float:
    return max(a, b, c)

# 11. Fahrenheit til Celsius


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

# 12. Reverser en streng


def reverse_string(s: str) -> str:
    # [start:stop:step] stop er ikke inkludert step er negativ for å gå tilbake
    return s[::-1]

# 13. Sjekk om liste er tom


def is_list_empty(list: list) -> bool:
    return len(list) == 0

# 14. Faktorial


def factorial(n: int) -> int:
  # ingen negativ tall
    if n < 0:
        raise ValueError("Faktorialen er ikke definert for negative tall.")

# range(2, n+1) → generates numbers 2, 3, …, n
# Start at 2 because multiplying by 1 is unnecessary(we already set result=1)
# result *= i → shorthand for result = result * i
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


"""
result = 1

i = 2 → result = 1 * 2 = 2

i = 3 → result = 2 * 3 = 6

i = 4 → result = 6 * 4 = 24

i = 5 → result = 24 * 5 = 120
"""

# 15. Summer en liste med tall


def sum_list(numbers: list[float]) -> float:
    return sum(numbers)

# 16. Fjern vokaler fra en streng


def remove_vowels(s: str) -> str:
    vowels = "aeiouyAEIOUYæøåÆØÅ"
    return "".join(char for char in s if char not in vowels)


if __name__ == "__main__":
    hello_world()
    greet("Fenriz")
    add_numbers(5, 7)
    print("Multiply:", multiply(3, 4))
    print("Is 10 even?", is_even(10))
    print("Circle circumference r=5:", circle_circumference(5))
    print("Strings equal?", strings_equal("abc", "abc"))
    print("3600 seconds =", seconds_to_hours_minutes(3600))
    print("Word count:", count_words("Hei på deg!"))
    print("Max of 3, 7, 5:", max_of_three(3, 7, 5))
    print("100F in Celsius:", fahrenheit_to_celsius(100))
    print("Reverse 'Python':", reverse_string("Python"))
    print("Is list empty?", is_list_empty([]))
    print("Factorial of 5:", factorial(5))
    print("Sum of list:", sum_list([1, 2, 3, 4]))
    print("Remove vowels 1:", remove_vowels("Dette er en test ÆÆ ÅÅ ØØ"))
