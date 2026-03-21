# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def f(s1, s2, n):
    if s1 < s2:
        return n
    else:
        return f(s2, s1, n * -1)


print(f("mickey", "donald", 7))
