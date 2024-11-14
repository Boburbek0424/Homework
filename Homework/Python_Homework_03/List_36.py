List=[12,32,12,421,13] #given integer numbers list
Total=0
for i in range(len(List)):
    if List[i]%2==0:
        Total+=List[i]
print("Sum of all even numbers:",Total)    