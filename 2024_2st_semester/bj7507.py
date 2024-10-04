from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 10000
s = "Scenario #"

for i in range(int(input())):
    q = []
    n = int(input())
    for _ in range(n):
        d, st, ed = map(int, input().split())
        heappush(q, (ed, st, d))

    # 끝나는 시간 가장 빠른 것끼리 가능 
    ans = 0
    st = [0] * (n+1)
    for _ in range(n):
        ced, cst, j = heappop(q)
        if cst >= st[j]:
            ans += 1
            st[j] = ced 


    print(f'{s}{ i+1}:')
    print(ans )
    print()

