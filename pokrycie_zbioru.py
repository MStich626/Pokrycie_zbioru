from numpy import matrix
import numpy as np

# Lista wartości jednostkowych danej usługi
wartosci = []

# Ogólna cena za wszystkie usługi danej firmy
price = [300,60,600,500]

# Lista wszystkich możliwych usług
uslugi = ['A','B','C','D','E']

# Wynik algorytmu (wybrane firmy)
wybrane_firmy = []

# Słownik wejściowy firm z usługami
arr = {'P0':['A','C','E'],
       'P1':['B','D'],
       'P2':['A','D'],
       'P3':['B','C','E']}

for a in range(0,3):
    k = 0
    numbers = [int(klucz[1:]) for klucz in arr.keys()]
    print(numbers)

    # Stworzenie listy wartości
    for i in numbers:
        wartosci.append(price[k]/len(arr['P'+str(i)][:]))
        k+=1
    print("Wartości: ",wartosci)

    # Posortowanie wartości
    wartosci_sort = sorted(wartosci)
    print("Posortowane wartosci: ",wartosci_sort)

    # Wyznaczenie minimalnej wartości jednostkowej
    minimum = wartosci_sort[0]
    print("Minimum: ",minimum)

    # Wyznaczenie minimalnej pozycji
    pozycja_min = 0
    for i in range(0,len(wartosci_sort)):
        if minimum == wartosci[i]:
            pozycja_min = i
            break
    wybrane_firmy.append('P' + str(pozycja_min))
    print("Minimalna pozycja: ",pozycja_min)

    # Wyznaczenie brakujących usług
    roznica = list(set(uslugi) - set(arr['P' + str(pozycja_min)]))
    print("roznica: ", roznica)
    print("Wybrane firmy: ", wybrane_firmy)

    uslugi = list(set(uslugi) - set(arr['P' + str(pozycja_min)]))
    # Warunek zakończenia algorytmu
    if len(roznica) == 0:
        break

    # Usunięcie wybranych usług
    del arr['P' + str(pozycja_min)]
    del wartosci[pozycja_min]
    del price[pozycja_min]

    print("arr: ",arr)
    print("wart: ",wartosci)


"""
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