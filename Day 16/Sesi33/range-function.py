print('')
x = range(5)
for n in x:    
    print(n)

print('')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'z' in i:
        break
    print(i)

print('')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

print('')
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

print('')
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.')             