my_dict = {"a": 5, "b": 10, "c": 15, "d": 20}
condition = int(input("Enter condition for value: "))
filtered_dict = {key: value for key, value in my_dict.items() if value > condition}
print(filtered_dict)
