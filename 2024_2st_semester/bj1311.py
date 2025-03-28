from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF =  sys.maxsize

# 일, 사람, 일종류 = cw, i, j = i가 j일을 cw만큼든다.
# 겹치지 않게 최소를 구하는 문제 = N이 적으므로 비트마스킹?>
n = int(input())
q = []
for _ in range(n):
    w, i, j = map(int, input().split())
    heappush(q, (w, i, j))

ta = {}
while q:
    
    w, i, j = heappop(q)
    if w not in ta:
        ta[w] = 
    