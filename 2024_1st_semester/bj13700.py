#시간복잡도 계산: heap연산을 통해 각 정점에서 2개의 경우의 수 2V이므로 O(N logN)이다.
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 1e9

n, s, d, f, b, k = map(int, input().split())
ma = [INF] * (n+1)

police = list(map(int, input().split()))
for i in police:
    ma[i] = -1


q = []
heappush(q, [0, s])

while q:

    cw, cn = heappop(q)
    if cn == d:
        break

    for i in [cn + f, cn -b]:
        if i <= 0 or i > n or ma[i] == -1:
            continue

    
        if ma[i] > cw + 1:
            ma[i] = cw + 1
            heappush(q, [cw + 1, i])


if ma[d] == INF:
    print('BUG FOUND')
else:
    print(ma[d])