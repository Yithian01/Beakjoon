from heapq import heappop, heappush
import sys
input = sys.stdin.readline
q = []

n, m = map(int, input().split())

high =[0] + list(map(int,input().split()))
for idx, v in enumerate(high):
    if idx == 0:
        continue

    heappush(q, (-v, idx))


ma = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    if high[s] > high[e]:
        s, e = e, s 

    ma[e].append(s) 


ans = [1] * (n+1) 
while q: 
    _, no = heappop(q) 
    for i in ma[no] :
        ans[i] = max(ans[i], ans[no] + 1)


for i in range(1, n+1):
    print(ans[i])