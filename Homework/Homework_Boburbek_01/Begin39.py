A,B,C=map(int,input("A,B va C koeffisentlarni kiriting(A,B,C): ").split(','))
D=B**2-4*A*C
x1=(-B+D**0.5)/(2*A)
x2=(-B-D**0.5)/(2*A)
print("x1 va x2:",x1,"and",x2)