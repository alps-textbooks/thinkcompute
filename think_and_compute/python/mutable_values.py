# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def append_one(l):
    l.append(1)
    return l


my_list = list()
my_list.append(2)
print(my_list)  # list([2])

result = append_one(my_list)
print(my_list)  # list([2, 1])
print(result)  # list([2, 1])
