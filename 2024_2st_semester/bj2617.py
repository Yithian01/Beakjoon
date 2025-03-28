import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ma = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    
    # a가 b보다 크다. 즉 나보다 작은 것을 표현
    ma[a][b] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if ma[i][k] == 1 and ma[k][j] == 1:
                ma[i][j] = 1
# 플로이드 워샬로 관계맺어주기

ans = 0
for i in range(1, n+1):
    up, down = 0, 0

    # i가 기준 j는 i보다 작음을 표현한 것
    for j in range(1, n+1):
    
        if i == j:
            continue

        if ma[i][j] == 1: # i가 j보다 크다.
            up +=1
        
        if ma[j][i] == 1:
            down += 1 # i가 j보다 작다.

    
    if up > n // 2 or down > n // 2:
        ans += 1

print(ans)