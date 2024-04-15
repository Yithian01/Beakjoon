# 트리이므로 사이클 없다.
# 시간 복잡도 계산: O(VE)? 10^5*10^5 => 10^10 이거 틀릴 것 같다.
import sys
input = sys.stdin.readline


n = int(input())
ma = [[] for _ in range(n+1)]
ans = [0] * (n+1)
vi = [False] * (n+1)
vi[1] = True

for _ in range(n-1):
    k, v = map(int ,input().split())
    ma[k].append(v)
    ma[v].append(k)


q = [1] 

while q:
    tmp = []
    for cn in q:
        for j in ma[cn]:
            if not vi[j]:
                vi[j] = True
                ans[j] = cn
                tmp.append(j)

    q = tmp

for i in range(2, n+1):
    print(ans[i])
