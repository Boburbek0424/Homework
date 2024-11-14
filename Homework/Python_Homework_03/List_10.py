Length=int(input("The number of elements: "))
List=[input(f"Enter the {i+1} - element: ") for i in range(Length)]
print(sorted(List))
# List.sort()
# print(List)