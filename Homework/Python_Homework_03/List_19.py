List=['12','32','41','12','324','23'] #consider it as given list
Element=input("Enter element to change: ")
NewElement=input("Enter element to change with: ")
for i in range(len(List)):
    if List[i]==Element:
        List[i]=NewElement
print("New list:",List)
