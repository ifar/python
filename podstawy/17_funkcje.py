

# Funkcja, która:
# nie przyjmuje żadnych argumentów
# nie zwraca żadnej wartości
# jedynie wykonuje te instrukcje, które są zapisane w ciele funkcji
def przykladowa_definicja_funkcji():
    print("Pierwsza instrukcja, którą wywołuje ta funkcja")
    zmienna = 10
    print("Wypisanie wartości zmiennej: {}".format(zmienna))


# Funkcja, która:
# przyjmuje 2 argumenty
# nie zwraca żadnej wartości
# jedynie wykonuje instrukcje, które są zapisane w ciele funkcji
def funkcja_przyjmujaca_argumenty(argument_1, argument_2):
    suma = argument_1 + argument_2
    print("Wynik sumy dla {} oraz {} wynosi: {}".format(argument_1, argument_2, suma))


# Funkcja, która:
# przyjmuje 1 argument
# zwraca wartość (return)
def funkcja_zwracająca_wartość(argument):
    potega_liczby_2 = pow(2, argument)
    return potega_liczby_2


# wywołanie funkcji bez argumentów
przykladowa_definicja_funkcji()

# wywołanie funkcji z argumentami
funkcja_przyjmujaca_argumenty(1, 2)

# wywołanie i wykorzystanie wartości, którą zwraca funkcja
print("Wynik potegowania: {}".format(funkcja_zwracająca_wartość(3)))


