my_tuple = (1, 2, 3, 1, 4, 1, 5)
Multiply=int(input("Enter the number of times: "))
my_list=[]
for i in range(len(my_tuple)):
    my_list.extend([my_tuple[i]]*Multiply)
print(my_list)