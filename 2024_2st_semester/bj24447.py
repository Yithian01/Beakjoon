import sys
from collections import deque
input = sys.stdin.readline
'''
    방문 순서 = t
    시작 정점t = 1, 시작 깊이d = 0
    시작 정점t = 1, 미방문 깊이d = -1

    모든 노드에서 t*d 의 합 

'''

n, m, r = map(int, input().split())
ma =[[] for _ in range(n+1)]
vi = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    ma[a].append(b)
    ma[b].append(a)


for i in range(1, n+1):
    ma[i].sort()

ans = 0
cnt = 1
q = deque()
q.append((r, 1, 0)) # 노드 , 순서, 깊이 
vi[r] = 1

while q:
    cn, ct, cd = q.popleft()
    ans += (ct * cd)

    for nn in ma[cn]:
        if vi[nn] == 0:
            vi[nn] = 1
            cnt += 1
            q.append((nn, cnt, cd + 1))
            
print(ans)