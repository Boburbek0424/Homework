List=[12,31,423,12,323,1] #example list
n=len(List)
if n%2==0:
    print("Middle values:",List[n//2-1],"and",List[n//2])
else:
    print("Middle value:",List[n//2])
