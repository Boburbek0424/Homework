def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
List=[12,42,12,42,12] #given list
if bubble_sort(List)==List:
    print("Sorted")
else:
    print("Not sorted")