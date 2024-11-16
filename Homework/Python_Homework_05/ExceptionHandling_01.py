def Dividing(x,y):
    try:
        result=x/y
        print("Result is",result)
    except ZeroDivisionError:
        print("Can't divide by zero")
x=1
y=0
Dividing(x,y)