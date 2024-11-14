Length=int(input("Enter number of elements in your list: "))
List=[]
for i in range(Length):
    List.append(input(f"Enter your {i+1}-element: "))
if List:
    print("The last element",List[Length-1])
else:
    print("List is empty")

    
    






