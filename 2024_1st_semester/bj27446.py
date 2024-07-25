import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
ma = list(map(int, input().split()))
q = []

# (1) m장만큼 정리 
# (2) 1 ~ n까지 빠진 페이지 있는지 확인 
# (3) 빠진 페이지 인쇄해야 함
for i in range(1, n+1):
    if i not in ma:
        q.append(i)


# 1, 2, 6, 8
ans, cnt = 7, 0
for i in range(1, len(q)):
    ans -= 7
    ans += min(14, 5 + ((q[i] - q[i-1] + 1) * 2))

if len(q) == 0:
    print(0)
else:
    print(ans)