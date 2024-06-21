# 예제 1) 같은 경우 

# 13으로 팔 떄 3명 전부가 산다. ==> 13 * 3 
# 22으로 팔 때 2명이 산다. ==> 22 * 2
# 35로 팔 때 1명만 산다. => 35

#시간 복잡도 계산: O(N^2)
import sys
input = sys.stdin.readline


q = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    q.append((a,b))


q.sort(key = lambda x : (x[0], x[1]))
ans = [0, 0]

for i in range(n):
    a = q[i][0] # 가격을 나타냄 
    res = 0
    for j in range(i, n): #현재 가격을 최대로 하는 사람들 순서대로 이므로 무조건 가능

        tmp = a - q[j][1] #배송비가 있다면 손해이므로 비교해야 한다.
        if tmp >= 0:
            res += tmp
    
    if ans[1] < res:
        ans[1] = res
        ans[0] = a


print(ans[0])