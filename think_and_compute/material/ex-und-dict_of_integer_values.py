# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def g(s):
    result = dict()
    for c in s:
        if c not in result:
            result[c] = 0
        result[c] = result[c] + 1
    return result.get("o")


print(g("Bologna"))
