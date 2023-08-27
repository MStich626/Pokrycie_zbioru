# Import bibliotek
from numpy import matrix
import numpy as np

# Lista wartości jednostkowych danej usługi
wartosci = []

# Lista wszystkich możliwych usług
uslugi = ['A','B','C','D','E']

# Wynik algorytmu (wybrane firmy)
wybrane_firmy = []

# Słownik wejściowy firm z usługami
arr = {'P0':['A','D',60],
       'P1':['A','E',70],
       'P2':['B','C','E',120],
       'P3':['C','E',30],
       'P4':['B','D',80]}



# Iterator wybranych firm
a = 0

# Ogólny koszt
koszt = 0

# Lista wybrancyh wszystkich uslug
koncowe_uslugi =[]

# Główna pętla
while(True):

    # Stworzenie listy wartości
    r = 0
    l_wartosci = []
    for klucz, wartosc in arr.items():
        l_wartosci.append(len(wartosc)-1)
        wartosci.append((wartosc[-1]) / l_wartosci[r])
        r += 1
    print("wartosci:  ",wartosci)

    # Posortowanie wartości
    wartosci_sort = sorted(wartosci)
    print("Posortowane wartosci: ",wartosci_sort)

    # Wyznaczenie minimalnej wartości jednostkowej
    minimum = wartosci_sort[0]
    print("Minimum: ",minimum)

    # Wyznaczenie firmy o najlepszej cenie
    for key, values in arr.items():
        if values and values[-1] == minimum*(len(values)-1):
            wybrane_firmy.append(str(key))
            koszt += minimum*(len(values)-1)

    print("arr:  ",arr)

    # Wyznaczenie brakujących usług
    print("a:", a)
    print("wybranefirm od a:  ", wybrane_firmy[a])
    print("Wybrane firmy: ", wybrane_firmy)
    if wybrane_firmy[a] in arr:
        wybrane_uslugi = arr[wybrane_firmy[a]][:-1]

    roznica = list(set(uslugi) - set(wybrane_uslugi))
    koncowe_uslugi.extend(wybrane_uslugi)

    unique_values = set(koncowe_uslugi)

    # Konwersja zbioru z powrotem na listę
    unique_list = list(unique_values)
    print("riznicaaa: ", unique_list)
    print("Wybrane usługi:", wybrane_uslugi)
    print("roznica: ", roznica)
    print("Wybrane firmy: ", wybrane_firmy)
    print("arr:  ",arr)


    ####
    for key in arr:
        arr[key] = [value for value in arr[key] if value not in wybrane_uslugi]

    del arr[wybrane_firmy[a]]
    a += 1
    print("arr:  ",arr)

    del wartosci[:]


    keys_to_remove = []

    for key, values in arr.items():
        if len(values) == 1:  # Sprawdzamy, czy liczba wartości wynosi 1
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del arr[key]

    print("-----------------------")
    print("Całkowity koszt: ",koszt," zł")
    print("Wybrane firmy: ",wybrane_firmy)
    if len(unique_list) == len(uslugi):
        break

"""
## Testowa tablica
# A B C D E F G H I J
# 1 2 3 4 5 6 7 8 9 10

uslugi = ['A','B','C','D','E','F','G','H','I','J']
arr = {'P0':['A','D','H','J',715],
       'P1':['B','E','I',582],
       'P2':['A','F','I',745],
       'P3':['D','H',500],
       'P4':['E','H','I',610],
       'P5':['A','C','G','J',241],
       'P6':['F','G','J',310],
       'P7':['B','E','H',72],
       'P8':['C','D','F','I',1166],
       'P9':['B','C','G',38]
}


"""
