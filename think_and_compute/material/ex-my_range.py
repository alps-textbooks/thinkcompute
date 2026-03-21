# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_my_range(stop_number, expected):
    result = my_range(stop_number)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_range(stop_number):
    l = list()
    while stop_number > 0:
        stop_number = stop_number - 1
        l.insert(0, stop_number)
    return l


# Tests
print(test_my_range(0, []))
print(test_my_range(1, [0]))
print(test_my_range(4, [0, 1, 2, 3]))
