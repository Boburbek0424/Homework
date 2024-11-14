Length=int(input("Enter the number of elements: "))
List=[]
for i in range(Length):
    List.append(int(input(f"Enter the {i+1}-element(integer): ")))
Min=0
for i in range(Length):
    Min=List[0]
    if List[i]<Min:
        Min=List[i]
print("The minimum number is",Min)