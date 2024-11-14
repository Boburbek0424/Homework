my_set={1,2,312,34}
even_set=set()
for num in my_set:
    if num%2==0:
        even_set.add(num)
print("Even numbers' set:",even_set)