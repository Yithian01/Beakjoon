# 진입간선 체크하면 될 것 같은데
# 진입간선 없는 걸로다가 시작
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = [[] for _ in range(n+1)]
ig = [0] * (n+1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1):
        ig[tmp[i+1]] += 1
        ma[tmp[i]].append(tmp[i+1])

q = deque()
for i in range(1, n+1):
    if ig[i] == 0:
        q.append(i)

if len(q) == 0:
    print(0)
    exit(0)

ans = []
while q:
    cn = q.popleft()
    ans.append(cn)

    for i in ma[cn]:
        ig[i] -=1
        if ig[i] == 0:
            q.append(i)

if len(ans) < n:
    print(0)

else:
    for i in ans:
        print(i)