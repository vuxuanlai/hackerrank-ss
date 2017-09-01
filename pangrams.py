#!/bin/python3
import sys, string

s = input().strip()

def check(str):
    az = string.ascii_lowercase
    for i in range(len(az)):
        if az[i] not in str.lower():
            return False
    return True

print("pangram" if check(s) else "not pangram")
