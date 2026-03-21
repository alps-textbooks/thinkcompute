# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

from re import sub


def cnt(mat_string):
    result = 0

    if len(mat_string) > 0:
        n = int(mat_string[0])

        if n % 2 == 0:
            return 1 + cnt(mat_string[1:len(mat_string)])
        else:
            return -1 + cnt(mat_string[1:len(mat_string)])
    
    return result

my_mat_string = sub(" +", "", input("Please provide your matriculation number: ").lower())
print("Result:", cnt(my_mat_string))
