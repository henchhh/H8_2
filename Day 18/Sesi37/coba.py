def square(nums):
    # result = []
    for num in nums:
        yield num*num
        # result.append(num*num)
    # return result
numsNew = [1,2,3,4,5].__iter__()
# print(next(square(numsNew)))
# print(next(square(numsNew)))       
# print(next(square(numsNew))) 
# print(next(square(numsNew)))       
# print(next(square(numsNew)))  

# squareRootGenerator = square(numsNew)
# for num in squareRootGenerator:
#     print(num)

# squareNums = [y*y for y in [1,2,3,4,5]]
squareNums = (y*y for y in [1,2,3,4,5])
print(next(squareNums))
print(next(squareNums))
print(next(squareNums))
print(next(squareNums))
print(next(squareNums))