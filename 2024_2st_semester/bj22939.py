import sys
from itertools import permutations
input = sys.stdin.readline
INF = 10 ** 9 


kind = ['J','C', 'B', 'W']
res = ["Assassin", "Healer", "Mage", "Tanker"]
st = [0, 0]
ed = [0, 0]
ma = []
tmp = [[] for _ in range(4)]
n = int(input())


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for i in range(n):
    s = input().rstrip()
    for idx, v in enumerate(s):
        if v == 'H':
            st = [i, idx]
        elif v == '#':
            ed = [i, idx]
        

        for k in range(4):
            if v == kind[k]:
                tmp[k].append([i, idx])

minVal = INF
ans = ''
for i in range(4):
    per = permutations( tmp[i], 3)
    for p in per:
        d = dist(st, p[0]) + dist(p[0], p[1]) + dist(p[1], p[2]) + dist(p[2], ed) 

        if minVal > d:
            minVal = d
            ans = res[i]

print(ans)