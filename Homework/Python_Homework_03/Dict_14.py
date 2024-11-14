my_dict={"age":29,"Name": "Husen","Month":"November","date":29}
Element=input("Enter the value to count keys: ")
Total=0
Values=[]
for key,value in my_dict.items():
    if str(value)==Element:
        Values.append(key)
print(Values)
