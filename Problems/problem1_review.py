"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""


# Helper method to test equality
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Create a function that produces the factorial of a number
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


# Todo: Test factorial function
fact = factorial(0)
assert_equals(fact, 1)

# Todo: Request a number from the user
n = int(input("Enter number "))

# Todo: Print a list of factorials from 0 to the given number
my_list = []
for i in range(0, n+1):
    y = factorial(i)
    my_list.append(y)

print(my_list)

