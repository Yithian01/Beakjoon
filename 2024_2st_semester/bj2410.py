n = int(input())
lst = [1 << i for i in range(21)]
print(len(lst))
mod = 1000000000
dp = [0] * (n + 1)
dp[0] = 1
for i in lst:

    print(f'i = {i}, n = {n}')
    if i <= n :
        for j in range(i, n + 1):
            print(f'j = {j} ')
            dp[j] += dp[j - i]

    else:
        break


print(dp[1 : 11])
print(dp[n] % mod)