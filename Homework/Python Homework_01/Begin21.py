#imported from Begin20 question:
x_1,y_1=map(int,input("Birinchi nuqta kordinatasi(x1,y1): ").split(','))
x_2,y_2=map(int,input("Ikkinchi nuqta kordinatasi(x2,y2): ").split(','))
x_3,y_3=map(int,input("Uchinchi nuqta kordinatasi(x3,y3): ").split(','))
a=(((x_2-x_1)**2+(y_2-y_1)**2))**0.5
b=(((x_3-x_2)**2+(y_3-y_2)**2))**0.5
c=(((x_3-x_1)**2+(y_3-y_1)**2))**0.5
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))**0.05
print("Yuzasi:",S,";","Perimetri:",p)