def enrollment_stats():
    global students
    global tuitionfee
    univer_name=[]
    students=[]
    tuitionfee=[]
    Values=eval(input("Enter the list: "))
    for word in Values:
        univer_name.append(word[0])
        students.append(word[1])
        tuitionfee.append(word[2])
    return students,tuitionfee
def mean(list:list):
    mean=sum(list)/len(list)
    return mean
def median(list:list):
    sorted_list=sorted(list)
    n=len(list)
    if n%2==1:
        median=sorted_list[n//2]
    else:
        median=(sorted_list[n//2]+sorted_list[n//2-1])/2
    return median
enrollment_stats()
print("******************************")
print(f"Total students: {sum(students)}")
print(f"Total tuition fee: {sum(tuitionfee)}")
print('\n')
print(f"Student mean: {mean(students)}")
print(f"Student median: {median(students)}")
print('\n')
print(f"Tution mean: {mean(tuitionfee)}")
print(f"Tution median: {median(tuitionfee)}")
    