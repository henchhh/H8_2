def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

print('')
print(list(my_generator()))
my_generator_new = my_generator()
print(next(my_generator_new))
print(next(my_generator_new))
print(next(my_generator_new))

# print('')
# for char in my_generator():
#   print(char)

# print('')
# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1


# for i in infinite_sequence():
#   print(i, end=" ")