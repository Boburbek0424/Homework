List=['12','312','12','23333']
print([List[len(List)-1]] + List[1:len(List)] + [List[0]])
#        last one               middle           first one