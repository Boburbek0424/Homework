A,B,C=map(int,input("A,B va C sonlarini kiriting(A,B,C): ").split(','))
X=C
C=B
B=A
A=X
print("Yangi qiymatlar:",A,B,C)
