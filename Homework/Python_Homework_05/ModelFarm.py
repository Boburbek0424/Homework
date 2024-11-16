class Animal:
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        if age < 0:
            raise ValueError("Age can't be less than zero")
        self.age = age

    def eating(self):
        print(f"{self.name} is eating.")

    def sleeping_time(self):
        print(f"{self.name} sleeps 7 hours a day.")

    def make_sound(self):
        print(f"{self.name} can make a sound.")

class Cow(Animal):
    def __init__(self, name: str, species: str, age: int, gives: str) -> None:
        super().__init__(name, species, age)
        self.gives = gives

    def eating(self):
        print(f"{self.name} eats plants.")

    def sleeping_time(self):
        print(f"{self.name} sleeps 4 hours a day.")

    def make_sound(self):
        print("Ma-ma-ma")

    def what_it_gives(self):
        print(f"{self.name} gives {self.gives}.")

class Dog(Animal):
    def __init__(self, name: str, species: str, age: int, color: str) -> None:
        super().__init__(name, species, age)
        self.color = color

    def eating(self):
        print(f"{self.name} eats meat.")

    def sleeping_time(self):
        print(f"{self.name} sleeps 6 hours a day.")

    def make_sound(self):
        print("Bark-bark!")

    def describe_color(self):
        print(f"{self.name} is {self.color}.")

class Fish(Animal):
    def __init__(self, name: str, species: str, age: int, taste: str) -> None:
        super().__init__(name, species, age)
        self.taste = taste

    def eating(self):
        print(f"{self.name} eats small organisms.")

    def sleeping_time(self):
        print(f"{self.name} sleeps 1 hour a day.")

    def make_sound(self):
        print("Splsh-splsh!")

    def describe_taste(self):
        print(f"{self.name} is {self.taste}.")

cow = Cow(name="Miya", species="Cow", age=2, gives="milk")    
cow.eating()            
cow.what_it_gives()     
