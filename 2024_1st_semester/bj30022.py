from heapq import heappop, heappush
import sys
input = sys.stdin.readline


aa = []
bb = []

diff = []


n ,a, b = map(int, input().split())
for i in range(n):
    k, v = map(int, input().split())
    aa.append(k)
    bb.append(v)


    di = k - v
    heappush(diff, (di, i))


ans = 0
for i in range(a):
    _, idx = heappop(diff) 
    ans += aa[idx]

for i in range(b):
    _, idx = heappop(diff) 
    ans += bb[idx]
    

print(ans)