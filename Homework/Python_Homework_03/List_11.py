Length=int(input("The number of elements: "))
List=[input(f"Enter the {i+1} - element: ") for i in range(Length)]
New_List=list(set(List))
print(New_List)