# 들어오는 indgree 가 없는 것을 먼저 처리해주면 된다.
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())

ans = [] 
id = [0] * (n+1)


ma = [[] for _ in  range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    id[b] +=1
    ma[a].append(b)
    
q = deque()
for i in range(1, n+1):
    if id[i] == 0:
        q.append(i)


while q:
    cn = q.popleft()
    ans.append(cn)

    for i in ma[cn]:
        if id[i] >= -1:
            id[i] -=1
        
        if id[i] == 0:
            q.append(i)

print(*ans)