List=[12,3,124,23,34,23] # given list
Element=int(input("Enter the given element: "))
Total=[]
for i in range(len(List)):
    if List[i]==Element:
        Total.append(i)
print("All indices list(empty list if element not in the list):",Total)