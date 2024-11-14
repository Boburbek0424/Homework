Length=int(input("Enter the number of elements: "))
List=[]
for i in range(Length):
    List.append(int(input(f"Enter the {i+1}-element(integer): ")))
Max=0
for i in range(Length):
    Max=List[0]
    if List[i]>Max:
        Max=List[i]
print("The maximum number is",Max)