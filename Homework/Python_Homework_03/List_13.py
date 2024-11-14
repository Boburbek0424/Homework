Length=int(input("The number of elements: "))
List=[input(f"Enter the {i+1} - element: ") for i in range(Length)]
print("Index of the value is",List.index(input("Enter a value to find its index: ")))
