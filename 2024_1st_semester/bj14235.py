# 최대 힙 이용해서 힙이 비어있으면 -1 출력 아니면 heappop

# 시간 복잡도 계산 : 5 * 10^3 * log 5*10^3 => 5 * 10^3 * 13 => 6 * 10^4
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

