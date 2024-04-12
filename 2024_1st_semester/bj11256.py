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
