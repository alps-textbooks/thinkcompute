# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_my_reversed(input_list, expected):
    result = my_reversed(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_reversed(input_list):
    l = list()
    for item in input_list:
        l.insert(0, item)
    return l


# Tests
print(test_my_reversed([], []))
print(test_my_reversed([1], [1]))
print(test_my_reversed([1, 2, 4, 3, 4, 7, 2], [2, 7, 4, 3, 4, 2, 1]))
print(test_my_reversed(["a", "b", "c", "d"], ["d", "c", "b", "a"]))

