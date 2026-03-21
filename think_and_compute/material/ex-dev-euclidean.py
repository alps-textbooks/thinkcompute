# SPDX-FileCopyrightText: 2025 Silvio Peroni <essepuntato@gmail.com>
#
# SPDX-License-Identifier: ISC

# Test case for the function
def test_euclidean(r, s, expected):
    result = euclidean(r, s)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def euclidean(r, s):
    if r == s:
        return r
    elif r < s:
        return euclidean(r, s - r)
    else:
        return euclidean(r - s, s)

        
        
# Tests
print(test_euclidean(1, 1, 1))
print(test_euclidean(1, 2, 1))
print(test_euclidean(1, 3, 1))
print(test_euclidean(3, 2, 1))
print(test_euclidean(3, 3, 3))
print(test_euclidean(3, 9, 3))
print(test_euclidean(15, 6, 3))