my_set={1,2,312,34}
Element=int(input("Enter the element to add: "))
if Element in my_set:
    print("Already in the set")
else:
    my_set.add(Element)
    print("Added")
    print(my_set)