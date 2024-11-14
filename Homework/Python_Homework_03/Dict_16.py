my_dict={"age":29,"Name": "Husen","Month":"November","date":29}
for key in my_dict.keys():
    if isinstance(key,dict):
        print("Contains dictionary")
        break
    else:
        print("Does not contain any dictionary")
        break
