from numpy import matrix
import numpy as np
"""
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



# Lista wartości jednostkowych danej usługi
wartosci = []

# Ogólna cena za wszystkie usługi danej firmy
price = [300,600,600,50]

# Lista wszystkich możliwych usług
uslugi = ['A','B','C','D','E']

# Wynik algorytmu (wybrane firmy)
wybrane_firmy = []

# Tablica wejściowa firm z usługami
arr = [['A','C','E'],['B','D'],['A','D'],['B','C','E','A']]

# Stworzenie listy wartości
for i in range(0,len(arr)):
    wartosci.append(price[i]/len(arr[i][:]))
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
# wybrane_firmy.append(pozycja_min)
print("Minimalna pozycja: ",pozycja_min)

# Wyznaczenie brakujących usług
roznica = list(set(uslugi) - set(arr[pozycja_min]))
# Usun
arr.pop(pozycja_min)

print("roznica: ", roznica)
print("arr: ",arr)