# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def f(x, y):
    if x <= 0 and y != 0:
        return x / y 
    else:
        return y / x


print(f(3, 0))
