class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    def __add__(self,otherWeight):
        return (f"Berat Miles adalah {self.weight}, sedangkan yang lain adalah {otherWeight.weight}")


miles = JackRussellTerrier("Miles", 4, 50)
print(miles.weight, 100)