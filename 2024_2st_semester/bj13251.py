import sys
input = sys.stdin.readline


n = int(input())
ma = list(map(int, input().split()))
m = int(input())

le = sum(ma)
ans = 0.0

for i in ma:
    res = 1.0
    if i < m:
        continue
    for j in range(m):

        res = res * (i-j) / (le - j)
    ans += res

print(f'{ans:.11f}')

