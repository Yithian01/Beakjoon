from heapq import heappop, heappush
import sys
input = sys.stdin.readline
dir = [1, 0, -1]
INF = 1e9

n, m = map(int, input().split())
ma = [1e9] * (n+1)
for _ in range(m):
    s = int(input())
    ma[s] = -1


if ma[2] == -1:
    print(-1)
    exit(0)

ma[1] = 0
ma[2] = 1
q = []# jump, speed, index
q.append((1, 1, 2))
while q:
    
    j, s, cn = heappop(q)
    for ds in dir:
        ns = s + ds
        nn = cn + ns

        if ns <= 0 or nn > n or ma[nn] == -1 :
            continue

        if nn > cn:

            ma[nn] = min(ma[nn], j + 1)
            heappush(q, (j+1, ns, nn ))
            


if ma[n] == INF:
    print(-1)
else:
    print(ma[n])