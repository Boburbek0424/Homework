my_set={1,2,312,34}
odd_set=set()
for num in my_set:
    if num%2==1:
        odd_set.add(num)
print("Even numbers' set:",odd_set)