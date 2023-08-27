from numpy import matrix
import numpy as np

# Lista wartości jednostkowych danej usługi
wartosci = []

# Ogólna cena za wszystkie usługi danej firmy
#price = [60,70,120,30,80]

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

a = 0
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

    print("arr:  ",arr)

    # Wyznaczenie brakujących usług
    print("a:", a)
    print("wybranefirm od a:  ", wybrane_firmy[a])
    print("Wybrane firmy: ", wybrane_firmy)
    if wybrane_firmy[a] in arr:
        wybrane_uslugi = arr[wybrane_firmy[a]][:-1]

    roznica = list(set(uslugi) - set(wybrane_uslugi))
    if len(roznica) == 0:
        break
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
"""

# Warunek zakończenia algorytmu
#if len(roznica) == 0:
   # break

# Usunięcie wybranych usług


print("arr: ",arr)
print("--------------------------------")







for i, klucz in enumerate(arr):
    wartosci.append(price[i] / len(arr[klucz]))
"""

"""TESTY

# Creating array step I
price_vector_temp = input("Enter price vector (use space to separate): ")
price_vector = price_vector_temp.split( )
rows = int(input("Enter number of rows:"))
cols = rows
arr = []

# Creating array step II
for i in range(rows):
    row_input = input(f"Enter data for first row {i+1} (use space to separate): ")
    row_values = row_input.split( )
    row = [int(value) for value in row_values]
    arr.append(row)
print(arr)
"""
"""
suma = []
wartosci = []
price = [200,60,4,500]
arr = [[1,0,0,1],[1,1,1,0],[1,0,1,0],[0,1,0,1]]



for i in range(0, len(arr)):
    suma.append(sum(arr[i]))
    wartosci.append(price[i] / suma[i])
wartosci.append(pow(10,10))

print(wartosci)

min_var = [1000,1000,10000,10000,10000,10000]
pozycja = [10,10,10,10,10,10,10]
min_var[0] = wartosci[0]
pozycja[0] = 0
for i in range(1,len(wartosci)):
    if (wartosci[i] < min_var[i-1]) and wartosci[i] != 0:
        min_var[i-1] = wartosci[i]
        pozycja[i] = i
    elif (wartosci[i] == min_var[i-1]) and wartosci[i] != 0:
        min_var[i] = wartosci[i]
        pozycja[i+1] = i+1
print(min_var)
for i in range(0,len(min_var)):
    if min_var[i] != min_var[i+1]:
        del min_var[i+1:]
        break
print(min_var)
print(pozycja)

#x1 = np.min(wartosci[np.nonzero(wartosci)])
"""
"""
def algorythm(price,services):
    wydatek = 0
    firmy = []
    j = 1
    suma = []
    wartosci = []
    l_uslug = len(services)
    l_firm = l_uslug

    while(True):
        for i in range(0, len(services)):
            suma.append(sum(services[i]))
            wartosci.append(price[i] / suma[i])

        if sum(suma) == 0:
            break

        else:
            x1 = np.min(wartosci[np.nonzero(wartosci)])
            if len(x1) > 1:
                x1 = x1[random(0:len(x1), 1)]
            wspl < - which(uslugi[, x1] == 1 )
            uslugi[wspl,] < - 0
            suma[x1] < - 0
            wartosci[x1] < - 0
            uslugi[, x1] < - 0
            wydatek < - wydatek + cena[x1]
            firmy[j] < - x1
            j = j + 1


algorythm(arr)
"""