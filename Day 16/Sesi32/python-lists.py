a = ['foo', 'bar', 'baz', 'qux']
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

b =['baz', 'qux','bar','foo']
c=b

print("Is a same as b?", a==b)
print("Is b same as c?", b==c)