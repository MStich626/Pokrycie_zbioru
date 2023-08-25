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
suma = []
wartosci = []
price = [20,60,40,50]
arr = [[1,0,0,1],[1,1,1,0],[1,0,1,0],[0,1,0,1]]
for i in range(0, len(arr)):
    suma.append(sum(arr[i]))
    wartosci.append(price[i] / suma[i])

#print(wartosci[wartosci != 0])
#x1 = np.min(wartosci[np.nonzero(wartosci)])
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