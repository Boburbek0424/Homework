my_dict={"age":29,"month":"november","Salary":2900}
Key=input("Enter the key to remove: ")
result=my_dict.pop(Key,"Not found")
if result != "Not found":
    print(f"Removed value:{result}")
else:
    print(result)