slownik_pesel = {90132873390: "Adam Kowalski",
                 80121283922: "Jacek Stefanowski",
                 64092199112: "Stefan Skowronek",
                 54010199221: "Adam Smolarek",
                 91111184394: "Sebastian Chrzanowski"}

ilosc_elementow = len(slownik_pesel)
element_o_podanym_kluczu = slownik_pesel[91111184394]
dodanie_nowego_elementu = slownik_pesel[32090114281] = "Adam Kolejny"
del slownik_pesel[54010199221]  # usunięcie elementu o kluczu: 54010199221
slownik_pesel[80121283922] = "Jacek Inny"  # edycja wartości elementu o kluczu 80121283922




