# 메모리 12 * 10^6 까지  <--- 제한
# 시간 10^8 까지 <---- 제한 


# 왜 크면 가장 작은 수를 뺄까? <----- 큰 거에서 유지만 시켜주면 되기 때문에
# 5 7 9 12 15 
# 13
# 7 9 12 13 15

# 시간 복잡도 계산 : O(N log N) =>  10^6 * 20 => 2 * 10^7 정도
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


q = []
n = int(input())

for _ in range(n):
    ma = list(map(int, input().split()))
    for i in ma:
        if len(q) < n:
            heappush(q, i)
        else:
            if q[0] < i:
                heappop(q)
                heappush(q, i)

print(q[0])
