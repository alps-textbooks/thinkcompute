# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC


def ni(s1, s2):
    if s1 in s2 and s2 in s1:
        return False
    else:
        return True


print(ni("27", "42"))
