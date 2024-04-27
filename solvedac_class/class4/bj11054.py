import sys
input = sys.stdin.readline


n = int(input())
ma = list(map(int, input().split()))
re_ma = ma[::-1]

up = [1] * (n)
down = [1] * (n)

for i in range(n):
    for j in range(i):
        if ma[i] > ma[j]:
            up[i] = max(up[i], up[j]+1)
        

        if re_ma[i] > re_ma[j]:
            down[i] = max(down[i], down[j] + 1)

ans = 0
down = down[::-1]

for i in range(n):
    tmp = up[i] + down[i] -1
    ans = max(ans, tmp)

print(ans)