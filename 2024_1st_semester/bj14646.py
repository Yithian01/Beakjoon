import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))
vi = [0 for _ in range(n + 1)]


ans, cnt = 0, 0
for i in range(n):
    cn = ma[i]
    if vi[cn] == 0:
        vi[cn] += 1
        cnt += 1

    elif vi[cn] == 1:
        vi[cn] += 1
        cnt -= 1
    
    else:
        continue

    ans = max(ans, cnt)

print(ans)