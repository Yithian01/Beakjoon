import sys
input = sys.stdin.readline

ans = 0
q = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if b == 0:
       ans += len(q)
       q = []

    else:
        if b not in q:
            q.append(b)


ans += len(q)
print(ans)