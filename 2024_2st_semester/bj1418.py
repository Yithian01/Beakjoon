import sys
input = sys.stdin.readline
INF = 10**5

# 에라토스테네스를 이용해서 각 배열 idx에 해당하는 최고 소인수분해값을 넣어준다.
num =  [_ for _ in range(INF + 1)]
vi = [False] * (INF + 1)

for i in range(2, INF + 1):
    if vi[i]:
        continue


    cnt = 2
    vi[i] = True
    while i * cnt <= INF:
        num[i * cnt] = i
        vi[i * cnt] = True
        cnt += 1


n = int(input())
m = int(input())
ans = 0
for i in range(1, n+1, 1):
    if num[i] <= m:
        ans += 1

print(ans)