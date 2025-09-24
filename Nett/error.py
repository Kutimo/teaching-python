""" try:
    x = int("hello")
except ValueError:
    print("Ikke en int")
 """


try:
    num = int(input("Skriv inn et nummer: "))
except ValueError:
    print("Input er ikke et gyldig nummer!")
else:
    print(f"Du skriv inn tallet: {num} ")
finally:
    print("Denne kjører alltid")
