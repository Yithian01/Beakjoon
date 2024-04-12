from heapq import heappush, heappop
import sys
input = sys.stdin.readline


q = []

n = int(input())
for _ in range(n):
    ma = list(map(int,input().split()))

    if ma[0] == 0:
        if len(q) == 0:
            print(-1)
        else:
            ans = heappop(q)
            print(-ans)

            
    else:
        for i in ma[1:]:
            heappush(q, -i)

