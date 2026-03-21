# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_exponentation(base_number, exponent, expected):
    result = exponentation(base_number, exponent)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def exponentation(base_number, exponent):
    if exponent == 0:
        return 1
    else:
        return base_number * exponentation(base_number, exponent - 1)


# Tests
print(test_exponentation(3, 4, 81))
print(test_exponentation(17, 1, 17))
print(test_exponentation(2, 0, 1))
print(test_exponentation(0, 15, 0))
print(test_exponentation(0, 0, 1))
