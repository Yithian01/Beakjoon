# 담을 수 있는 모든 보석들이 들어가게 된다.
# 4 4
# 보석 = [(1, 100), (2, 200), (13, 300), (10, 500)]
# 가방 = [10, 10, 10, 14] 이라면 
# 10에 담을 수 있는 보석 => [100, 200, 500] 이 tmp에 담기게 된다.
# 현재 10에서 넣을 수 있는 최고인 500을 ans에 담는다. 
# 다음 10에서 넣을 수 있는 것은 앞에서 같기에 while 문을 돌지 않는다.
# 들어있는 tmp에서 최대 수인 200을 더한다.
# 반복한다.
# 14에서 300이 들어가게 되고 
# 최고 수인 300을 더해준다.

#시간 복잡도 계산: O(n * n log n) 
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

ma, q = [], []
n, k = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    ma.append((a,b))

for _ in range(k):
    a = int(input())
    q.append(a)

ma.sort()
q.sort()

ans = 0
tmp = []

for i in q:                    # TTTFFF
    while ma and ma[0][0] <= i: # 제일 가벼운 보석이 가방 용량에 들어간다면
        heappush(tmp, -ma[0][1]) # 가격을 최소힙으로 
        heappop(ma)
    
    if tmp:
        ans -= heappop(tmp)
    
print(ans)