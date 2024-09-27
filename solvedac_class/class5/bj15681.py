# root부터 dfs로 가장 하단 노드부터 1로 바꾸고 더한다. 
# 가장 말단 노드는 1이 될 것이고 
# 올라올 수록 +1 씩 될 것이다. 
# 요청 받는대로 vi[i]를 출력하면 된다.

# 시간복잡도 계산: O(N+M) -> 10^5 + 10^5
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(cn):
    global vi
    vi[cn] = 1
    for i in q[cn]:
        if vi[i] == -1:
            vi[cn] += dfs(i)
    
    return vi[cn]



n, st, v = map(int, input().split())
q = [[] for _ in range(n+1)]
vi = [-1] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    q[a].append(b)
    q[b].append(a)

dfs(st)
for _ in range(v):
    m = int(input())
    print(vi[m])