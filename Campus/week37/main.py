""" Oppgave 3.4 Lag en funksjon som tar en annen funksjon som parameter, noen argumenter og et forventet resultat, og som returnerer sant hvis det faktiske resultatet stemmer overens med det forventede resultatet, ellers usant.
 """


def test_input():
    while True:
        user_input = input("Write a number: ")
        if validate_int(user_input) == True:
            break
        else:
            print("not a int:")


def validate_int(i):
    if i.isdigit():
        return True
    else:
        return False


test_input()
