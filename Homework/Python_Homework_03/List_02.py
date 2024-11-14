Length=int(input("Enter the number of elements: "))
List=[]
for i in range(Length):
    List.append(int(input(f"Enter the {i+1}-element(integer): ")))
Total=0
for i in range(Length):
    Total=Total+List[i]
print("The sum of the numbers:",Total)


