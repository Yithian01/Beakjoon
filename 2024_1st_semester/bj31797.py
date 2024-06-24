from collections import deque
import sys
input = sys.stdin.readline


dq = deque()
q = []
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    q.append((a, (i+1)))
    q.append((b, (i+1)))

q.sort(key= lambda x : x[0])
for i in q:
    dq.append(i)

ans = 0
for i in range(n):
    ans = dq.popleft()
    dq.append(ans)

print(ans[1])