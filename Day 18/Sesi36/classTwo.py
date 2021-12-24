class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# print(Dog()) => ERROR
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print(buddy.name)
print(buddy.age)
print(buddy.species)