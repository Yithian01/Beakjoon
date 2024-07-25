# bisect_right - bisect_left = 어떤 배열에 내가 원하는 숫자가 몇개 있는지 알 수 있다.
# a = [1,2,2,2,2,4] 라고 하자, 편의상 br, bl로 칭한다.
# br(a, 2) -> 5 ( 5번째 index에 할당) -> a배열에서 2가 추가로 들어갈떄의 위치(제일 오른쪽) 5
# bl(a, 2) -> 1 ( 1번째 index에 할당) -> a배열에서 2가 처음으로 나오는(제일 왼쪽)곳은 1

# br - bl = 4 실제로 2는 4개가 있음 --> 이 동작을 2log(n) 으로 가능 

# 나올 수 있는 모든 경우의 수를 저장해 놓는다. 최대 n이 10^3이므로 10^6으로 전처리

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
q1 = list(map(int,input().split()))
m = int(input())
q2 = list(map(int,input().split()))

dp1, dp2 = [], []

for i in range(n):
    for j in range(i + 1, n+1):
        dp1.append(  sum(q1[i:j])  )


for i in range(m):
    for j in range(i + 1, m+1):
        dp2.append(  sum(q2[i:j])  )


dp1.sort()
dp2.sort()

ans = 0
for i in range(len(dp1)):
    tmp = t - dp1[i]
    le = bisect_left(dp2, tmp)
    ri = bisect_right(dp2, tmp)

    ans += ri - le

print(ans)