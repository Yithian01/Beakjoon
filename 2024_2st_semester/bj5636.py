import sys
input = sys.stdin.readline
INF = 100000
# 시간복잡도 계산 : k log k + n^2 ---> but k = 10^5 n = 10^2 정도 즉 k log k가 더 크다.

li = []
ma = [False] * (INF + 1)
for i in range(2, INF + 1):
    if not ma[i]:
        ma[i] = True
        li.append(i)

    cnt = 1
    while i * cnt <= 100000:
        ma[i * cnt] = True
        cnt += 1


while True:
    n = input().rstrip()
    if n == '0':
        break

    ans = -1
    for st in range(len(n)):
        for ed in range(st +1, len(n)):
            tmp = int(n[st:ed])
            if tmp in li and ans < tmp:
                ans = tmp
        
    print(ans)
