import random
num_items = 5          
start_range = 1      
end_range = 100   
my_set=set(random.sample(range(start_range,end_range),num_items))
print(my_set)
