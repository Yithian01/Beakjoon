import sys
from itertools import combinations 
# 내림차순은 조합으로 판별난다는 생각을 공략을 보고 알았다.
# 조합: 똑같은 것 배제 
# 0 ~ 10의 숫자중에 3개 선택 시 
# (10/3) * (9/2) * (8/1) = 120
# 최대 10자리수의 조합이므로 
# 10개 중에 1개 선택 
# 10개 중에 2개 선택 
# 10개 중에 3개 선택 
#  . . . . . 
# 10 개중에 10개 선택 
# 이 가장 높은 복잡도를 가진다.

# 시간 복잡도 계산: O(10^3 * log 10^3) => 10^4 정도로 줄어든다.

input = sys.stdin.readline

n = int(input())
ans = []


for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        ans.append(int(''.join(map(str, num))))
ans.sort()


if len(ans) <= n:
    print(-1)
else:
    print(ans[n])