print('')
raining = False
print("Let's go to the", 'beach' if not raining else 'library')

print('')
raining = True
print("Let's go to the", 'beach' if not raining else 'library')

print('')
age = 12
s = 'teen' if age < 21 else 'adult'
print(s)

print('')
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')