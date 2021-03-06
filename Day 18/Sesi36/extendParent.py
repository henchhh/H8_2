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
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


miles = JackRussellTerrier("Miles", 4)
print(miles.speak()) # => Miles says Arf

print(miles.speak("Grrr")) # => Miles says Grrr