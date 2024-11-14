my_dict={"age":29,"month":"november","Salary":2900}
my_dict2={"name":'Husen',"Phone":"Samsung","Ismarried":True}
new_dict=dict(my_dict|my_dict2)
print(new_dict)
#other method
# my_dict={"age":29,"month":"november","Salary":2900}
# my_dict2={"name":'Husen',"Phone":"Samsung","Ismarried":True}
# new_dict=my_dict.copy()
# new_dict.update(my_dict2)
# print(new_dict)