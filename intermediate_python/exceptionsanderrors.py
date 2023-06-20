# Errors and Exceptions

# Syntax Error

# print("Hello World)

# Name Error

# print(hello)

# Type Error

# print(5 + "s")

# Index Error

# l = [1, 2, 3]
# print(l[4])

# ValueError

# s = "hello"
# print(int(s))

# KeyError

# d = {}
# print(d['foo'])

# AttributeError

# l = [1, 2, 3, 4]
# l.push(5)

# Raising an Exception

# x = -5

# if x < 0:
#     raise Exception('x should be positive')

# assert (x >= 0), 'x is not positive'

# try:
#     a = 8 / 0
# except Exception as e:
#     print(e)

# try:
#     a = 8 / 0
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("Everything is fine")
# finally:
#     print("Cleaning up...")

class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
