from heapq import heappush, heappop
import sys
input = sys.stdin.readline

ma = []
n, m, k = map(int, input().split())
for _ in range(k):
    a, b = map(int, input().split()) # 선호도, 레벨
    ma.append([a, b])


q = []
ma.sort(key = lambda x : (x[1], -x[0]))

ans = -1
res = 0
for i in ma:
    heappush(q, i[0])
    res += i[0]
    
    if len(q) == n:
        if res >= m:
            ans = i[1]
            break

        else:
            res -= heappop(q)


print(ans)