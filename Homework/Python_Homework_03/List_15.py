List=[2,4,6,8,10,12,43,54232,12] # given list
Total=0
for i in range(len(List)):
    if List[i]%2==0:
        Total+=1
print("Total number of even numbers:",Total)
