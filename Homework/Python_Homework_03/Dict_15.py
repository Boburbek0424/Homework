key=[1,2,3,4,5]
value=['today','tomorrow','random','number','item']
my_dict={}
for i in range(len(key)):
    my_dict[key[i]]=value[i]
print(my_dict)

# or other method

key=[1,2,3,4,5]
value=['today','tomorrow','random','number','item']
my_dict=dict(zip(key,value))
print(my_dict)