# List of service unit values
list_of_values = []

# List of possible services
services = ['A','B','C','D','E']

# Algorithm results (selected companes)
selected_companes = []

# Input dictionary (services and price on last place)
arr = {'P0':['A','D',60],
       'P1':['A','E',70],
       'P2':['B','C','E',120],
       'P3':['C','E',30],
       'P4':['B','D',80]}

# Iterator selected companies
a = 0

# Price
price = 0

# List selected services
final_services =[]

# Main loop
while(True):

    # Create temporary list of values
    r = 0
    temp_list_of_values = []
    for key, values in arr.items():
        temp_list_of_values.append(len(values)-1)
        list_of_values.append((values[-1]) / temp_list_of_values[r])
        r += 1

    # Sorting list of values
    sorted_values = sorted(list_of_values)

    # Select minimum from values
    minimum = sorted_values[0]

    # Finding company with lowest price
    for key, values in arr.items():
        if values[-1] == minimum*(len(values)-1):
            selected_companes.append(str(key))
            price += minimum*(len(values)-1)

    # Finding of missing services
    if selected_companes[a] in arr:
        selected_services = arr[selected_companes[a]][:-1]

    # Adding selected services to final services
    final_services.extend(selected_services)

    # Remove duplicate from final services
    unique_values = set(final_services)

    # Convert back to list
    unique_list = list(unique_values)

    # Remove from dictionary values, which contains in selected company
    for key in arr:
        arr[key] = [value for value in arr[key] if value not in selected_services]

    # Remove key - value (company), which we chose
    del arr[selected_companes[a]]
    a += 1

    # Clear list of values before next iteration
    del list_of_values[:]

    # Remove key - value (company) from dictionary where is only price (0 services , len(price) = 1)
    keys_to_remove = []
    for key, values in arr.items():
        if len(values) == 1:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del arr[key]

    # Loop ending condition
    if len(unique_list) == len(services):
        break

# Showing info
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
