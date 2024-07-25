import sys
input = sys.stdin.readline
#in_range = lambda r, c : 0 <= r < n and 0 <= c < n # 범위 조절 함수
INF = 1e9

n, m = map(int, input().split())
ma = list(map(int, input().split()))

tmp, ans, cnt = 0, INF, 0
st, ed = 0, 0 
while ed < n:
    tmp += ma[ed]
    cnt += 1
    ed += 1
    
    if tmp >= m:
        ans = min(ans, cnt)
        while st < ed:
            tmp -= ma[st]
            cnt -= 1
            st += 1
            if tmp < m:
                break
            else:
                ans = min(ans, cnt)

if ans == INF:
    print(0)
else:
    print(ans)