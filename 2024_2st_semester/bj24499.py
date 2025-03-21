import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = [0] * (n + m - 1)
for idx, val in enumerate(list(map(int, input().split()))):
    ma[idx] = val

for i in range(n, n+m-1):
    ma[i] = ma[i - n]

res = sum(ma[0:m])
ans = res
st = 0
for ed in range(m, n + m - 1):
    res += ma[ed]
    res -= ma[st]
    st += 1
    ans = max(ans, res)

print(ans)