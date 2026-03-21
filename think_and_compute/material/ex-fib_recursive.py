# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_fib(n, expected):
    result = fib(n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Tests
print(test_fib(0, 0))
print(test_fib(1, 1))
print(test_fib(2, 1))
print(test_fib(7, 13))
print(test_fib(-15, 0))
