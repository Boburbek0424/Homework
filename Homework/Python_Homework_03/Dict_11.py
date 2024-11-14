my_dict={"age":29,"Name": "Husen","Month":"November"}
Key=input("Enter the key to uptade its value: ")
if Key in my_dict:
    my_dict[Key]=input("Enter value to replace with: ")
    print("Updated!")
else:
    print("Key not found!")