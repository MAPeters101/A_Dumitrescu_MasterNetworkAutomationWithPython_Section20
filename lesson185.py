
a, b = 3, 4
print( a is b)


print(id(a))
a += 3
print(a)
print(id(a))

numbers = [1, 2, 3]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))

nums = numbers.copy()
print(nums == numbers)
print(nums is numbers)
print(id(nums))
print(id(numbers))

