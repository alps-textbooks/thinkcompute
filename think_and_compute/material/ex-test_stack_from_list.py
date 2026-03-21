# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

from collections import deque


# Test case for the function
def test_stack_from_list(input_list, expected):
    result = stack_from_list(input_list)
    if expected == result:
        return True
    else:
        return False

# Code of the function
def stack_from_list(input_list):
    output_stack = deque()  # the stack to create

    # Iterate each element in the input list and add it to the stack
    for item in input_list:
        output_stack.append(item)

    return output_stack


# Three different test runs
print(test_stack_from_list([], deque()))
print(test_stack_from_list([1, 2, 3, 4, 5], deque([1, 2, 3, 4, 5])))
