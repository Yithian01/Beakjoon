import sys
sys.setrecursionlimit(10 **6)
input = sys.stdin.readline

ans = 0
def dfs(st, vi, cnt):
    global ans 
    ans = max(ans, cnt)

    for nn, we in ma[st]:
        if not vi[nn]:
            vi[nn] = True
            dfs(nn, vi, cnt + we )
   
    return 

n = int(input())
ma = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    ma[a].append((b, c))
    ma[b].append((a, c))


vi = [False] * (n+1)
vi[1] = True

dfs( 1, vi, 0)
print(ans)