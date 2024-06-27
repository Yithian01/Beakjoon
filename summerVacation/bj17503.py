# 정답이 안되는 경우를 열어라 FFFTTT 라면 => (0, ed)    0 ~ ed 
# while을 탈출했을 경우 닫힌 구간쪽이 정답이 될수 있는 것 
# (0, 9] = > 1 2 3 4 5 6 7 8 9

import sys
input = sys.stdin.readline

maxBeer = 1 << 31
n, m, k = map(int, input().split())
ma = []
for _ in range(k):
    a, b = map(int, input().split())
    maxBeer = max(maxBeer, b)
    ma.append((a,b))


ma.sort(key = lambda x : -x[0])

st, ed = 0, maxBeer   # FFFFFFTTTT   높을수록 될 가능성이 커진다. (0, maxBeer] 
while st + 1 < ed:
    mid = (st + ed) // 2
    tmp = 0 

    cnt = 0
    for i in ma:

        if mid >= i[1]: # 현재 mid(레벨) == 도수가 같다면
            tmp += i[0] # 현재 맥주 넣기 ( 가장 높은 선호도가 충족됨)
            cnt += 1

        if n == cnt:
            break

    if tmp >= m and cnt == n:
        ed = mid
    else:
        st = mid


if ed == maxBeer:
    print(-1)

else:
    print(ed)
