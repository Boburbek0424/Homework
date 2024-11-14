Length=int(input("The number of elements: "))
List=[input(f"Enter the {i+1} - element: ") for i in range(Length)]
To_Insert,Index=map(int,input("Enter a value and index(a,b): ").split(','))
List.insert(Index,To_Insert)
print(List)