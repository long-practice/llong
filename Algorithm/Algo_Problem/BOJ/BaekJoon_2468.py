# 2468
# 안전지대

import sys
from collections import defaultdict as dd
input = sys.stdin.readline

def Repr(a):
    if Set[a] == a:
        return a
    k = Repr(Set[a])
    Set[a] = k
    return k

def Join(a,b):
    Set[Repr(b)] = Repr(a)

def adj(p):
    yield p - w
    yield p - 1
    yield p + 1
    yield p + w

n = int(input())
w = n + 2

Set = {}

contour = dd(list)
for i in range(1, n+1):
    new = list(map(int, input().split()))
    for h, j in zip(new, range(i*w+1, (i+1)*w - 1)):
        contour[h].append(j)
heights = sorted(contour, reverse = True)
heights.pop()
fixed = []
cnt = 1
for h in heights:
    for k in contour[h]:
        Set[k]=k
    for p in contour[h]: # Connection change is made from added points(to both new and old components)
        for q in adj(p):
            if q in Set: Join(p, q)
    fixed = [p for p in fixed if Set[p] == p]
    for p in contour[h]:
        if Set[p] == p:
            fixed.append(p)
    cnt = max(cnt, len(fixed))

print(cnt)
