print('')
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


print('')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print('')
for k in d:
    print(d[k])

print('')
for k in d.values():
    print(k)

print('')
for k,v in d.items(): 
    print(k, ":", v)       

print('')
for k in d.items(): 
    print(k)                