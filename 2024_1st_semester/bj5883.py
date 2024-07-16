import sys
input = sys.stdin.readline

se = set()
ma = []
n = int(input())
for _ in range(n):
    a = int(input())
    se.add(a)
    ma.append(a)



ans = 0
while se:
    cn = se.pop()
    tmp = [ i for i in ma if i != cn]
    dp = [1] * n

    for i in range(1, len(tmp)):
        if tmp[i-1] == tmp[i] :
            dp[i] = dp[i-1] + 1 

    ans = max(ans, max(dp))


print(ans)