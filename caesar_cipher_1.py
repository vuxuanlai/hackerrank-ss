#!/bin/python3

import sys, string

n = int(input().strip())
s = input().strip()
k = int(input().strip())

az = string.ascii_lowercase*k
AZ = string.ascii_uppercase*k


def check(s):
    for i in range(len(s)):
        if s[i] in az or s[i] in AZ:
            if s[i].islower():
                s = replacer(s, check_index(s[i], 1), i)
            else:
                s = replacer(s, check_index(s[i], 2), i)
    return s


def check_index(value, type):
    if type == 1:
        return get_index(value, az)
    elif type == 2:
        return get_index(value, AZ)


def get_index(value, alphabet):
    index = 0
    for i in range(int(len(alphabet)/k)):
        if value == alphabet[i]:
            index = i
            break
    return alphabet[index + k]


def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

print(check(s))
