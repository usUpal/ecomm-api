# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b


# # using the generator to print the first 10 Fibonacci numbers
# for num in fibonacci(10):
#     print(num)
# defining a generator function
def my_generator():
    for i in range(10):
        yield i


# using the generator to lazily generate a sequence of values
# gen = my_generator()
# print(gen)
# for i in my_generator():
#     print(i)

# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)

# print(next(iterator))  # Output: 1
# print(next(iterator))  # Output: 2
# print(next(iterator))  # Output: 3
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
people = list(zip(names, ages))
print(people)
