# a를 index로 B를 연결된 값
# 열림 반열림 구간 종료조건에 대해서 

# 1) st < ed 
# 2) st + 1 < ed 


# (1)의 경우 정확한 위치를 찾는데에 사용된다.
# 예시) [4, 11, 12] 에서 6을 넣고 싶다. 원하는 위치는 1번 index
#  st = 0, ed = 3
#  mid = 1
#  11 > 6 이므로 F이다. ed = mid = 1
#  mid = 0 
#  4 < 6 이므로 T이다. st = mid + 1 =  1
#  
# st == ed가 같아졌으므로 이 동작은 i-1 < i < i+1 이것을 만족하는 식이 된다.

import sys
input = sys.stdin.readline


# 시간 복잡도 계산: N + N log N + k + (k * N) + N + N =>
# 10^5 => 10^2 => 2^7 * 2^10 => 2^17 이므로 10^7 * 17 => 10^8승 정도


ma = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ma.append((a,b))


ma.sort()
res = [ma[0][1]]
# index가 A, 값이 B라고 설정
# 현재 index까지의 LIS
dp = [0] * n 

for i in range(n):
    # 현재 index보다 신규로 들어오는 게 더 크다면 그냥 넣어주기 
    if res[-1] < ma[i][1]:
        res.append(ma[i][1])
        dp[i] = max(dp) + 1 
    else:
        
        st, ed = 0, len(res)
        while st < ed:
            mid = (st + ed) // 2 
            
            if res[mid] < ma[i][1]:
                st = mid + 1
            else:
                ed = mid

    
        # 내가 그 자리보다 작다는 건 a < x < b 가 성립 
        # 
        if res[st] >= ma[i][1]:
            res[st] = ma[i][1]
            dp[i] = st + 1 
        
        else:
            res[st] = ma[i][1]
        

            
ans = []


r = len(res) 
for i in range(n-1, -1, -1):
    if r == 0:
        break

    if dp[i] == r:
        ans.append(ma[i])
        r -= 1 


li = []
for i in ma:
    if i not in ans:
        li.append(i[0])

li.sort()
print(len(li))
for i in li:
    print(i)