# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

from re import sub


def rsel(full_name, mat_string):
    uniq = []
    for c in full_name:
        if c not in uniq:
            uniq.append(c)
    
    r = []
    i = len(mat_string) // 2
    if i > 0:
        n = int(mat_string[i])
        if n < len(uniq):
            r.append(uniq[n])
            new_full_name = full_name[0:n] + full_name[n+1:len(full_name)]
            new_mat_string = mat_string[0:n] + mat_string[n+1:len(mat_string)]
            r.extend(rsel(new_full_name, new_mat_string))
    
    return r

my_full_name = sub(" +", "", input("Please provide your full name: ").lower())
my_mat_string = sub(" +", " ", input("Please provide your matriculation number: ").lower())
print("Result:", rsel(my_full_name, my_mat_string))
