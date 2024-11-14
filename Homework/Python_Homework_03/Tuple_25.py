my_tuple=(1,4,23,45,32,23,12,1,21,2)
my_list=[]
for i in range(len(my_tuple)):
    if my_tuple[i] not in my_list:
        my_list.append(my_tuple[i])
print(tuple(my_list))
