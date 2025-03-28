from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF =  sys.maxsize

for tc in range(int(input())):
    n, m = map(int, input().split())
    ma = [[] for _ in range(m+1)]
    q = []
    heappush(q, (0, [0])) # 가중치, 노드

    for _ in range(n):
        a, b, c = map(int, input().split())
        ma[a].append((b, c))
        ma[b].append((a, c))

    vi = [INF] * (m+1)
    vi[0] = 0
    ans =( INF , [-1])
    while q:
        cw, cn = heappop(q)
        

        for nn, dw in ma[cn[-1]]:
            if nn == (m-1):
                if ans[0] > dw + cw:
                    ans = (dw + cw, cn + [nn])

            elif vi[nn] > cw + dw:
                vi[nn] = cw + dw
                heappush(q, (cw + dw, cn + [nn]))

        
    print(f'Case #{tc + 1}:', end=' ')
    for i in ans[1]:
        print(i, end=' ')
    print()
    