#https://www.hackerrank.com/challenges/sherlock-and-valid-string
#!/bin/python
from collections import Counter
import sys

def isValid(s):
    # Complete this function
    data_dict = {}
    if len(s) == 1: return "YES"

    s_count_all_char = Counter(s).values()
    s_count_char_value = Counter(s_count_all_char).values()
    if len(s_count_char_value) == 1: return "YES"

    for i in s:
        if not data_dict:
            data_dict[i] = 1
        else:
            if i in data_dict.keys():
                data_dict[i] = data_dict.get(i) + 1
            else:
                data_dict[i] = 1
    check = None
    for k, v in data_dict.items():
        sub = v - 1
        data_dict[k] = sub
        if sub != 0:
            for i in data_dict.values():
                if sub != i:
                    check = False
                    break
                else:
                    check = True
        else:
            data_temp = data_dict
            del data_temp[k]
            temp = list(data_temp.values())[0]
            for nk, nv in data_temp.items():
                if nv == temp:
                    check = True
                else:
                    check = False
                    break
        data_dict[k] = sub+1
        if check: return "YES"
    return "NO"

s = input().strip()
result = isValid(s)
print(result)
