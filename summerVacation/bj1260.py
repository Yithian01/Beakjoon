from collections import deque
import sys
input = sys.stdin.readline


def dfs(st, vi):
    print(st, end=' ')

    for i in ma[st]:
        if not vi[i]:
            vi[i] = True
            dfs(i, vi)
    
    
    return 
    


    
def bfs(st):
    q = deque() 
    q.append(st)

    vi = [False] * (n+1)
    vi[v] = True
    while q:
        cn = q.popleft()
    
        print(cn, end= ' ')
        for i in ma[cn]:
            if not vi[i]:
                vi[i] = True
                q.append(i)

    return 


n, m, v = map(int, input().split())
ma = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ma[a].append(b)
    ma[b].append(a)


for i in range(1, n+1): # 정렬
    ma[i].sort()

vi = [False] * (n+1)
vi[v] = True

dfs(v, vi)
print()
bfs(v)