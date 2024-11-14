List=[23,42,12,43] #given list
Index=int(input("Enter the index: "))
if Index>0 and Index<len(List):
    List[Index]=''
    print("Changed")
else: 
    print("Index out of range")

