List1=[12,4,23,532]
List2=[2,12]
New_list=List1+List2
for i in range(len(New_list)):
        for j in range(0, len(New_list) - i - 1):
            if New_list[j] > New_list[j + 1]:
                New_list[j], New_list[j + 1] = New_list[j + 1], New_list[j]
print("New sorted list:",New_list)
