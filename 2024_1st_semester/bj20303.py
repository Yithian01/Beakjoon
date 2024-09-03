from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]
INF= 1e9

def FIND(x):
    if un[x] != x:
        FIND(un[x])
    
    return un[x]


n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
un = [ _ for _ in range(n+1)]
q = []

for _ in range(m):
    a, b = map(int, input().split())
    q.append((a,b))

for a, b in q:
    
    na = FIND(a)
    nb = FIND(b)

    if na != nb:

        if na > nb :
            na, nb = nb, na
                    
        un[a] = na
        un[b] = na

ans = []
print(f'un = {un}')
for i in range(1, n+1):
    
    tmp = 0
    for j in range(1, n+1):
        