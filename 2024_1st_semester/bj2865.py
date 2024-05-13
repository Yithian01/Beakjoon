import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ma = [0] * (n+1)

for _ in range(m):
    li = list(map(float, input().split()))
    for i in range(0, len(li), 2):
        idx = int(li[i])
        ma[idx] = max(ma[idx], li[i+1])

ma.sort(reverse=True)
ans = 0
for i in range(k):
    ans += ma[i]

print(round(ans, 1))