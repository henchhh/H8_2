# Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30}

# items
print(d.items())

# keys
print(d.keys())

# values
print(d.values())

person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
print (someone_is_of_working_age)

someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)

print(someone_is_of_working_age)