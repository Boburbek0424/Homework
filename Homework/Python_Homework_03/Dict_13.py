my_dict={"age":29,"Name": "Husen","Month":"November"}
new_dict={}
for key,value in my_dict.items():
    new_dict[value]=key
print(new_dict)