from math import sqrt
class Vector:
    def __init__(self,*arguments:int):
        self.arguments=arguments
    
    def __str__(self):
        return f"Arguments: {self.arguments}"

    def __bool__(self):
        if not any(self.arguments):
            return False
        else:
            return True
        
    def __len__(self):
        return len(self.arguments)

    def __getitem__(self,key):
        return self.arguments[key]
    def __setitem__(self,key,value):
        my_list=list(self.arguments)
        my_list[key]=value
        self.arguments=tuple(my_list)
        return self.arguments
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("Can't add different size vectors")
        else:
            return Vector(*[a+b for a,b in zip(self.arguments,other.arguments)])
    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError("Can't add different size vectors")
        else:
            return Vector(*[a-b for a,b in zip(self.arguments,other.arguments)])
    def __mul__(self,other):
        if isinstance(other,Vector):
            if len(self) != len(other):
                raise ValueError("Can't add different size vectors")
            else:
                return Vector(*[a*b for a,b in zip(self.arguments,other.arguments)])    
        else:
            if isinstance(other,(int,float)):
                return Vector(*[value*other for value in self.arguments])
    def __truediv__(self,other):
          if isinstance(other,(int,float)):
                return Vector(*[value/other for value in self.arguments])

    def __abs__(self):
        return sqrt(sum(value ** 2 for value in self.arguments))

    def __eq__(self,other):
        return self.arguments==other.arguments

    def __neg__(self):
        return Vector(*(-arguments for arguments in self.arguments))
v1=Vector(1,4,6)
print(v1)
print(bool(v1))
print(bool(Vector(0,0)))
print(len(v1))
print(v1[1])
v1[1]=10
print(v1)
v2=Vector(3,7,2)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1*3)
print(v1/2)
print(abs(v1))
print(v1==Vector(1,10,6))
print(-v1)