# 위상 정렬? inCome을 세고 작은 것부터 시작하자
# heapq로 바꿨더니 바로 되었다.
# 바로 전의 것만 비교하는 것이 아니었다?!
#
# inCome 간선을 사용해서 위상 정렬
# 시간 복잡도 계산: O( NlogN)
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inCome = [0] * (n+1)
ma = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    ma[s].append(e)
    inCome[e] += 1

q = []
for i in range(1, n+1):
    if inCome[i] == 0:
        heappush(q, i)

ans = []
while q:
    cn = heappop(q)
    ans.append(cn)

    for nn in ma[cn]:
        
        inCome[nn] -= 1

        if inCome[nn] == 0:
            heappush(q, nn)
            

print(*ans)