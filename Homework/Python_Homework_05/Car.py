class Car():
    def __init__(self,YearModel:int,Make:str) -> None:
        self.YearModel=YearModel
        self.Make=Make
        self.Speed=0
    def accelerate(self):
        self.Speed+=5
    def brake(self):
        if self.Speed>=5:
            self.Speed-=5
        else:
            self.Speed=0
    def getSpeed(self):
        return self.Speed
Matiz=Car(2016,'GM')
Matiz.accelerate()
Matiz.accelerate()
Matiz.accelerate()
Matiz.accelerate()
Matiz.accelerate()
Matiz.brake()
Matiz.brake()
Matiz.brake()
Matiz.brake()
Matiz.brake()
print(Matiz.Speed) # or Matiz.getSpeed()
