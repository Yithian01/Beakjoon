import sys
input = sys.stdin.readline

def FIND(x):
    if num[x] != x:
        num[x] = FIND(num[x]) 

    return num[x]


n, m, k = map(int, input().split()) 
num = [i for i in range(n + 1)] 
ma = [0] + list(map(int, input().split())) 

for _ in range(m):
    a, b = map(int, input().split())
    
    a = FIND(a)
    b = FIND(b)

    if a != b:
        num[a] = b 


ta = [1] * (n + 1)
dp = [0] * (k)

for i in range(1, n + 1):
    a = FIND(i)
    if a != i:
        ma[a] += ma[i]
        ta[a] += ta[i]

for i in range(1, n + 1):
    if i == num[i]:
        for j in range(k - 1, ta[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - ta[i]] + ma[i])


print(max(dp))