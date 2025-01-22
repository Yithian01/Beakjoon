import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10 ** 5)

def dfs(m, be):
    cnt = 0

    if be != -1 and ma[m] != be:
        cnt += 1

    for i in node[m]:
        if not vi[i]:
            vi[i] = True
            cnt += dfs(i, ma[m])

    return cnt    


n = int(input())
ma = list(map(int, input().split()))  # 각 노드의 색
node = [[] for _ in range(n)]
vi = [False] * n  # 방문 여부

# 간선 정보 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)

vi[0] = True
ans = 0
if ma[0] != 0:
    ans = 1
ans += dfs(0, -1)
print(ans)