# 주소 : "https://www.acmicpc.net/problem/24498"
# 누적합)
 
# (1) 크기를 키울 수 있는 공간은 1 ~ n-2 이다. 맨처음과 맨끝을 제외한 곳!!
# (2) (1)을 돌아보며 자기 양 옆에 있는 탑의 크기를 비교한다.
#       양 옆에 있는 값 중 가장 작은 값이 0이라면 탑의 높이를 높힐 수 없으므로 cotinue
#
# (3) 양 옆중 가장 작은 값을 자기자신에 더한 값이 그 값이 가질 수 있는 최대값이다.

# (4) but n <= 2일 경우는 (1) ~ (3)을 시작하지 못한다. 그러므로 max(arr)을 해서 기본값 중 최대를  구해준다.

#시간복잡도 계산 : O(N)
import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int,input().split()))

ans = max(ma)
for i in range(1, n-1):
    tmp = min(ma[i-1], ma[i+1])
    if tmp == 0 :
        continue

    ans = max(ans, tmp + ma[i])

print(ans)
