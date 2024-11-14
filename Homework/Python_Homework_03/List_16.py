List=[23,8,10,3221,43,54232,12] # given list
Total=0
for i in range(len(List)):
    if List[i]%2==1:
        Total+=1
print("Total number of even numbers:",Total)
