import random

# --- 1. Random float between 0 and 1 ---
rand_float = random.random()
print("Random float 0-1:", rand_float)

# --- 2. Random float in a range ---
rand_uniform = random.uniform(10, 20)
print("Random float 10-20:", rand_uniform)

# --- 3. Random integer ---
rand_int = random.randint(1, 10)  # inclusive
print("Random integer 1-10:", rand_int)

# --- 4. Random choice from a list ---
colors = ["red", "green", "blue", "yellow"]
rand_color = random.choice(colors)
print("Random color:", rand_color)

# --- 5. Random sample of multiple unique items ---
numbers = [1, 2, 3, 4, 5]
sample_numbers = random.sample(numbers, 3)
print("Random sample of 3 numbers:", sample_numbers)

# --- 6. Random choice with possible repeats ---
repeated_choices = [random.choice(numbers) for _ in range(3)]
print("Random choices (with repeats):", repeated_choices)

# --- 7. Shuffle a list ---
deck = ["A", "2", "3", "4", "5"]
random.shuffle(deck)
print("Shuffled deck:", deck)

# --- 8. Seed for reproducible results ---
random.seed(42)
print("Seeded random integer 1-10:", random.randint(1, 10))  # always same output

# --- 9. Roll a dice function ---


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)

print("You rolled a dice:", roll_dice())
print("You rolled a 12-sided dice:", roll_dice(12))

# --- 10. Generate a list of 5 random integers 1-100 using list comprehension ---
random_list = [random.randint(1, 100) for _ in range(5)]
print("List of 5 random integers:", random_list)
