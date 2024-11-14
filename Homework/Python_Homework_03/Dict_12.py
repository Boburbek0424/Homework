my_dict={"age":29,"Name": "Husen","Month":"November","date":29}
Value=input("Enter the value to count occurance: ")
Total=0
Values=list(my_dict.values())
for Word in Values:
    if str(Word)==Value:
        Total+=1
print(Total)
