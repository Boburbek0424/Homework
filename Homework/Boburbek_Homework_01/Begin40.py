A1,B1,C1,A2,B2,C2=map(int,input("A1,B1,C1,A2,B2,C2 koeffisentlarni kiriting(A1,B1,C1,A2,B2,C2): ").split(','))
D=A1*B2-A2*B1
x=(C1*B2-C2*B1)/D
y=(A1*C2-A2*C1)/D
print("x va y'ning qiymati:",x,'va',y)