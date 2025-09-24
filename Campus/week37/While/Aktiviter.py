"""
Aktivitet 1 – Partall/Oddetall

Skriv et program som skriver ut alle partall mindre enn 10.
Hint: Bruk % for å sjekke resten når du deler på 2.

for i in range(1,10):
    if i % 2 == 0:
        print(i, end=" ")
"""
"""
Aktivitet 2 – Summer tall med while
Skriv et program som fortsetter å spørre brukeren om tall til de skriver 0, og deretter skriver ut summen.


sum=0

while True:
    number = int(input("Enter a number: "))
    sum +=number
    if number ==0:
        break

print(sum)
"""

"""
Aktivitet 3 – Tall mellom 1 og 100
Be brukeren skrive inn et tall mellom 1 og 100. Fortsett å spørre til tallet er gyldig. Skriv ut det.


while True:
    number = int(input("Enter a number between 1 and 100: "))
    if 0 < number <= 100:
        break
print(number)

"""
"""
Aktivitet 4 – Partall/Oddetall med continue

Skriv et program som skriver ut alle partall mindre enn 10.

Bruk continue

for i in range(10):
    if i%2==0:
        continue
    print(i)
"""

"""
Aktivitet 5 – Rund av tall

Be brukeren skrive inn et desimaltall og skriv ut taket (math.ceil) og gulvet (math.floor). 


"""

"""
Aktivitet 6 – Generer tilfeldige tall med math og random

Kombiner math og random: Generer et tilfeldig desimaltall mellom 0 og 1, multipliser med 10 og rund av med math.floor eller math.ceil.

"""

"""
Aktivitet 7 – PC gjetter et tall

Skriv et program der brukeren velger et tall mellom 1 og 100, og PC-en prøver å gjette det. Programmet skal:

-Be brukeren om å skrive inn et tall på en sikker måte. Hvis input ikke er et tall, spør igjen.
-Sjekke at tallet er innenfor tillatt område (1–100).
-La PC-en gjette tall tilfeldig helt til den treffer riktig tall.
-Tell hvor mange gjetninger PC-en bruker.
-Skriv ut antall forsøk når PC-en gjetter riktig.

Tips:

- Bruk .isdigit() for å sjekke om input er et tall.
- Bruk random.randint(min_nr, max_nr) for å lage gjetninger.

"""
