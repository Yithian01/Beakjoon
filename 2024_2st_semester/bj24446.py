from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, r = map(int, input().split())
vi = [INF] * (n+1)
ma = [[] for _ in range(n+1)]
q = deque()


vi[r] = 0
q.append(r)
for _ in range(m):
    a, b = map(int, input().split())
    ma[a].append(b)
    ma[b].append(a)

while q:
    cn = q.popleft()

    for nn in ma[cn]:
        if vi[nn] > vi[cn]:
            vi[nn] = vi[cn] + 1
            q.append(nn)


for i in range(1, n+1):
    if vi[i] == INF:
        print(-1)
    else:
        print(vi[i])