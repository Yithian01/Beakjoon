import sys
input = sys.stdin.readline
INF = 2e9


n = int(input())
ma = [int(input()) for _ in range(n)]


ma.sort()
cnt = 0

for num in ma:
    tmp = 1


    for i in range(num + 1, num + 5):
        if i in ma:
            tmp += 1

    cnt = max(cnt, tmp)
    if tmp >= 5:
        break    


if (5 - cnt) <= 0 :
    print(0)
else:
    print(5 - cnt)       