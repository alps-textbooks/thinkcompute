# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_binary_search(item, ordered_list, start, end, expected):
    result = binary_search(item, ordered_list, start, end)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def binary_search(item, ordered_list, start, end):
    if len(ordered_list) > 0 and start <= end:
        mid = (start + end) // 2
        mid_item = ordered_list[mid]
        if item == mid_item:
            return mid
        elif mid_item < item:
            return binary_search(item, ordered_list, mid + 1, end)
        else:
            return binary_search(item, ordered_list, start, mid - 1)


# Tests
print(test_binary_search(3, [1, 2, 3, 4, 5], 0, 4, 2))
print(test_binary_search("Denver", ["Alice", "Bob", "Catherine", "Charles"], 0, 3, None))
print(test_binary_search("Harry", ["Harry", "Hermione", "Ron"], 0, 2, 0))
print(test_binary_search("Harry", [], 0, 0, None))
