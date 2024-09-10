import os
import sys


def check(str):
    b = {}
    for i in str:
        b[i] = b.get(i, 0) + 1
    if len(b.keys()) == 2:
        for key in b.keys():
            if b[key] == 3:
                return "Yes"
    return "No"


n = int(input(""))
a = []
for i in range(n):
    a.append(input())
res = []
for s in a:
    res.append(check(s))
for ans in res:
    print(ans)
