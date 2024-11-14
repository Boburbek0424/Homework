List=[12,12,423] #given list
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1): # len(arr) - i - 1 for the efficient sort
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubble_sort(List)
print("Minimum element is",List[0])