# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


# Test case for the function
def test_partition(input_list, start, end, pivot_position, expected):
    p_value = input_list[pivot_position]
    result = partition(input_list, start, end, pivot_position)
    output = expected == result and p_value == input_list[result]

    for item in input_list[0:result]:
        output = output and item <= p_value
    for item in input_list[result + 1:len(input_list)]:
        output = output and item >= p_value

    return output


# Code of the function
def partition(input_list, start, end, pivot_position):
    pivot_value = input_list[pivot_position]

    swap_index = start - 1
    for index in range(start, end + 1):
        if input_list[index] < pivot_value:
            swap_index += 1
            if swap_index == pivot_position:
                pivot_position = index
            swap(input_list, swap_index, index)

    new_pivot_position = swap_index + 1
    swap(input_list, pivot_position, new_pivot_position)

    return new_pivot_position


def swap(input_list, old_index, new_index):
    cur_value = input_list[old_index]
    input_list[old_index] = input_list[new_index]
    input_list[new_index] = cur_value


# Run tests
print(test_partition([1, 2, 3, 4, 5], 0, 4, 0, 0))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 0, 2))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 2, 1))
print(test_partition([7, 5, 3, 1, 4], 0, 4, 4, 2))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 1, 8))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 0, 0))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 3, 6))
print(test_partition([1, 2, 2, 3, 9, 8, 4], 1, 2, 1, 1))
