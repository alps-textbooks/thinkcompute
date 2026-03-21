# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def t(x, y):
    return x + y - 2


print(t(5, t(3 + 2, 2)))
