Length=int(input("Enter number of elements in your list: "))
List=[]
for i in range(Length):
    List.append(input(f"Enter your {i+1}-element: "))
if List:
    print("The first element ",List[0])
else:
    print("List is empty")

    
    






