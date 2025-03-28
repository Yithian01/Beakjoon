import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
ma = [[0] * (n+1) for _ in range(n+1)]
node = [0] * (n+1)
q = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    ma[a][b] = 1
    ma[b][a] = 1
    q[a].append(b)
    q[b].append(a)

for i in range(1, n+1):
    node[i] = sum(ma[i])

ans = INF
for i in range(1, n+1):
    tmp = 0
    for j in q[i]:
        for k in range(1, n+1):
            if ma[j][k] == 1 and ma[i][k] == 1:
                ans = min(ans, node[i] + node[j] + node[k] - 6)

if ans == INF:
    print(-1)
else:
    print(ans )
                