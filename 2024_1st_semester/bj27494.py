import sys
input = sys.stdin.readline
dir = ['2','0','2','3']


n = int(input())

if n < 2023:
    print(0)
    exit(0)

# 누가봐도 비트마스킹인데.....
ans = 0
for i in range(2023, n+1):
    s = str(i)

    cnt ,tmp = 0, 0
    for i in range(len(s)):
        if cnt == 4:
            break

        if s[i] == dir[cnt]:
            tmp += 1
            cnt += 1
            continue


    if tmp == 4:
        ans += 1

print(ans)