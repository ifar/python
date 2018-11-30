zmienna_1 = 10
lista = ["Element 1", "Element 2", "Element 3"]
# Pętla iterująca tyle razy ile zadamy w range
# Zwraca numer itercji (rozpoczynając od 0)
for numer_iteracji in range(zmienna_1):
    print("Iteracja numer: {}".format(numer_iteracji + 1))

# Pętla iterująca tyle razy ile elementów w liście (lub innej kolekcji)
# Zwraca wartości kolejnych elementów listy
for element_listy in lista:
    print(element_listy)

# Pętla robiąca to samo, co ta wyżej, z jednym istotnym wyjątkiem:
# Oprócz elementu listy zwraca dodatkowo jego indeks w liście
# Indeks w liście oznacza kolejność elementu (zaczynając od 0)
for numer_iteracji, element_listy in enumerate(lista):
    print("Element numer: {} listy to: {}".format(numer_iteracji + 1,
                                                  element_listy))



