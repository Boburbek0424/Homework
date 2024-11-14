my_tuple = (1, 2, 3, 1, 4, 1, 5) # random tuple
Element=int(input("Enter the value to know indices: "))
Total=[]
for i in range(len(my_tuple)):
    if my_tuple[i]==Element:
        Total.append(i)
print("All indices list:",Total)