# Lista wartości jednostkowych danej usługi
list_of_values = []

# Lista wszystkich możliwych usług
services = ['A','B','C','D','E']

# Wynik algorytmu (wybrane firmy)
selected_companes = []

# Słownik wejściowy firm z usługami
arr = {'P0':['A','D',60],
       'P1':['A','E',70],
       'P2':['B','C','E',120],
       'P3':['C','E',30],
       'P4':['B','D',80]}

# Iterator wybranych firm
a = 0

# Ogólny koszt
price = 0

# Lista wybrancyh wszystkich uslug
final_services =[]

# Główna pętla
while(True):

    # Stworzenie listy wartości
    r = 0
    temp_list_of_values = []
    for key, values in arr.items():
        temp_list_of_values.append(len(values)-1)
        list_of_values.append((values[-1]) / temp_list_of_values[r])
        r += 1

    # Posortowanie wartości
    sorted_values = sorted(list_of_values)

    # Wyznaczenie minimalnej wartości jednostkowej
    minimum = sorted_values[0]

    # Wyznaczenie firmy o najlepszej cenie
    for key, values in arr.items():
        if values and values[-1] == minimum*(len(values)-1):
            selected_companes.append(str(key))
            price += minimum*(len(values)-1)

    # Wyznaczenie brakujących usług
    if selected_companes[a] in arr:
        selected_services = arr[selected_companes[a]][:-1]

    # Wyznaczenie wybranych usług
    if selected_companes[a] in arr:
        selected_services = arr[selected_companes[a]][:-1]

    # Dodanie wybranych usług do końcowych usług
    final_services.extend(selected_services)
    unique_values = set(final_services)

    # Konwersja zbioru z powrotem na listę
    unique_list = list(unique_values)

    # Usunięcie z całego słownika wartości, które były zawarte w wybranej firmie
    for key in arr:
        arr[key] = [value for value in arr[key] if value not in selected_services]

    # Usunięcie pary klucz-wartość (firma), które już wybraliśmy
    del arr[selected_companes[a]]
    a += 1

    # Wyczyszczenie listy wartości przed kolejną iteracją
    del list_of_values[:]

    # Usunięcie par klucz-wartość (firm) ze słownika, gdzie nie ma już potrzebnych usług
    keys_to_remove = []
    for key, values in arr.items():
        if len(values) == 1:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del arr[key]

    # Warunek kończący pętlę
    if len(unique_list) == len(services):
        break

# Wypisanie końcowych informacji
print("Final price: ",price," zł")
print("Selected companes: ",selected_companes)


"""
## Other data (longer)
# A B C D E F G H I J
# 1 2 3 4 5 6 7 8 9 10

services = ['A','B','C','D','E','F','G','H','I','J']
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
