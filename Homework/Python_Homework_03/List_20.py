List=[32,43,523,12,43,43] #consider it as given list
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubble_sort(List)
print(List[len(List)-2])