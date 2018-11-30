zmienna_1 = 10
zmienna_2 = 20

if zmienna_1 < zmienna_2:
    print("Tekst zostanie wyświetlony jeżeli zmienna_1 jest mniejsza niż zmienna_2")

if zmienna_2 <= zmienna_1:
    print("Tekst zostanie wyświetlony jeżeli zmienna_2 jest mniejsza bądź równa zmiennej 1")

if zmienna_1 == zmienna_2:
    print("Tekst zostanie wyświetlony jeżeli zmienna_1 jest równa zmiennej 2")

if zmienna_1 >= zmienna_2:
    print("Tekst zostanie wyświetlony jeżeli zmienna_1 jest większa bądź równa zmiennej 2")
else:
    print("Jeżeli powyższy warunek (IF) nie zostanie spełniony, to wyświeli się ten napis "
          "Oznacza to, że zmienna_1 jest mniejsza niż zmienna_2")

if zmienna_1 > 10 and zmienna_2 > 20:
    print("Tekst zostanie wyświetlony jeżeli:"
          "zmienna_1 jest większa niż 10"
          "i tym samym zmienna_2 jest większa niż 20")
elif zmienna_2 > 20 or zmienna_2 == 0:
    print("Jeżeli powyższy warunek (IF) nie zostanie spełniony, ale będzie spełnione:"
          "zmienna_2 jest większa niż 20"
          "LUB zmienna_2 jest równa zero")
else:
    print("Jeżeli dwa powyższe warunki nie zostaną spełnione, to wyświetli się ten napis. "
          "Oznacza to, że wspólny warunek: zmienna_1 jest większa niż 10 i zmienna_2 jest większa "
          "niż 20 jest niespełniony, dodatkowo oznacza to, że zmienna_2 jest mniejsza bądź równa "
          "20 oraz nie jest równa zero")





