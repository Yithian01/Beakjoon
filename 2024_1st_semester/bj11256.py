# 힙을 사용해서 각 상자의 넓이(r * c)를 큰 순서대로 정렬
# 큰 것부터 허용가능 넓이에서 0이 될때까지 뺀다.

# 시간 복잡도 계산 : n * log n => O(n log n) => 10 * 10^3 * log 10^3 => 10^4 * 10 => 10^5 
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    j, n = map(int,input().split())
    q = []

    for _ in range(n):
        a, b = map(int,input().split())
        tmp = a * b
        heappush(q, (-tmp))
    
    cnt = 0
    for _ in range(n):
        m = heappop(q)
        j -= -(m)
        cnt += 1
        if j <= 0:
            break
        
    print(cnt)
