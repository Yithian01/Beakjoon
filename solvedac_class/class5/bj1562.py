import sys
input = sys.stdin.readline
n = int(input())

nRan = 10
bRan = 1 << nRan
MOD = 10**9
dp = [[[0] * bRan for _ in range(nRan)] for _ in range(n+1)]


print(f'nRan = {nRan}')
print(f'bRan = {bRan}')

for i in range(nRan):
    for j in range(bRan):
        print(dp[i][j], end=" ")
    print()



