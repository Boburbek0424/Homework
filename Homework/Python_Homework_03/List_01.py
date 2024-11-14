Length=int(input("Enter number of elements in your list: "))
List=[]
for i in range(Length):
    List.append(input(f"Enter your {i+1}-element: "))
WordToFind=input("Enter character to find times of apperance: ")
Total=0
for i in range(Length):
    if WordToFind==List[i]:
        Total+=1
print("Enter number of apperance:",Total)





