Length=int(input("Enter number of elements in your list: "))
List=[]
for i in range(Length):
    List.append(input(f"Enter your {i+1}-element: "))
NewList=[]
for i in range(3):
    NewList.append(List[i])
print("The first three characters:", NewList)


    
    






