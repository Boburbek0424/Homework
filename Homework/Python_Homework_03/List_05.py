Length=int(input("Enter number of elements in your list: "))
List=[]
for i in range(Length):
    List.append(input(f"Enter your {i+1}-element: "))
WordToCheck=input("Enter character to check apperance: ")
if WordToCheck in List:
    print("It is here!")
else:
    print("It is not here")
    
    







