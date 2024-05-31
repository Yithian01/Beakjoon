import sys
input = sys.stdin.readline

ans = 0

n, k = map(int, input().split())
ma = [0] + list(map(int, input().split()))
ma.sort()

st, ed = 0, n
for i in range(k):
    if i % 2 == 0:
        ans += ma[ed] - ma[st]
        st += 1
    
    else:
        ed-=1

print(ans)

    