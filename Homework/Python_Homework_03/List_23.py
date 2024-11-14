List=[11,12,214,324,1212,323] #given integer numbers list
New_List=[] #new empty list
for i in range(len(List)):
    if List[i]%2==1:
        New_List.append(List[i])
print("Only even number:",New_List)