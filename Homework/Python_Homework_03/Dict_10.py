my_dict={"age":29,"month":"november","Salary":2900}
Key=input("Enter the key to show: ")
if Key in my_dict:
    Value=my_dict[Key]
    print(Key,Value)
else:
    print("Not found")