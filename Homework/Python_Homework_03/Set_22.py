my_list=[1,3,4,2,5,2]
my_set=set()
for i in range(len(my_list)):
    if my_list[i] not in my_set:
        my_set.add(my_list[i])
print(my_set)
