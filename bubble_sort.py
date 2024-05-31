my_array = [64, 34, 25, 12, 22, 11, 90, 5]

print(f"Given array: {my_array}")

n = len(my_array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Sorted array:", my_array)

# With improvement. Breaking off if no swaps are made
my_new_array = [7, 3, 9, 12, 11]

n = len(my_new_array)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_new_array)
