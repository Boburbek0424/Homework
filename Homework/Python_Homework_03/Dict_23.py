my_dict1 = {'a': 1, 'b': 'age', 'today': 'tuesday'}
my_dict2 = {'c': 'today', 'd': 'tuesday', 'b': 'none'}
if set(my_dict1.keys()) & set(my_dict2.keys()):
    print("Have key in common")
else:
    print("No common keys")
