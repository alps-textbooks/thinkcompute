# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_my_enumerate(input_list, expected):
    result = my_enumerate(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_enumerate(input_list):
    l = list()
    for i in range(len(input_list)):
        l.append((i, input_list[i]))
    return l


# Tests
print(test_my_enumerate([], []))
print(test_my_enumerate(["a", "b", "c"], [(0, "a"), (1, "b"), (2, "c")]))
