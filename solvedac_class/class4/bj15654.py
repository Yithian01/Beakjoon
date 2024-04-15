# 형변환 사용
# set -> 중복 방지 
# heapq -> 순서 정렬 
# 시간 복잡도 계산 : nCm + n log n 
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ma = list(map(int,input().split()))
ma = sorted(ma)
vi = [False] * (n+1)
se = set()


q = []
def bt():
    if len(q) == m:
        tmp = tuple(q)
        se.add(tmp)

    else:
        for i in range(n):
            if vi[i] : continue 

            vi[i] = True
            q.append(ma[i])
            bt()
            vi[i] = False
            q.pop()
            
bt()
pq = []
for i in se:
    heappush(pq, list(i))

for _ in range(len(pq)):
    print(*heappop(pq), sep=' ')