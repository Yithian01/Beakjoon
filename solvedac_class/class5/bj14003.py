import sys
input = sys.stdin.readline
# 이분탐색을 통해 LIS를 만들고 -->  N log N 
# 해당 되는 인덱스와 현재값을 dp에 저장 ---> N


# 까다로운 case는 [10 ,20, 30, 6, 7, 60, 5, 8, 9] 같은 사이에 낀 case입니다.
# LIS --> 최대 길이만큼만 길어질 것, 만약 작은 것들이 들어온다면 원래 위치에 대체되는 것임
# dp --> 어떤 수가 들어갔을 때 최장길이에서 어느 위치에 해당되는지 정보를 담고 있음 
# dp = [(0, 10), (1, 20), (2, 30), (0, 6), (1, 7), (3, 60), (0, 5), (2, 8), (3, 9)]
# 앞에서부터 구하면 오류 가능성 있음 뒤에서부터 구해야 함 
# 9 8 7 6 이렇게 결정될 것임

# 시간 복잡도 계산 : N log N + N => 2* 10^7 + 10^6정도 => O(N log N)

n = int(input())
ma = list(map(int, input().split()))

li = [ma[0]]
dp = [(0, ma[0])]


# TTTFFFFF  가장 오른쪽의 F를 찾는다?    ( ] 
def BS(num):
    st = 0
    ed = len(li)
    
    while st + 1 < ed:  # 종료 조건: st와 ed가 인접
        mid = (st + ed) // 2
        if li[mid] < num:  # TTTFFF 조건: num보다 작은 구간을 탐색
            st = mid
        else:
            ed = mid

    # T가 되는 구간이 가장 오른쪽의 T일 경우 #
    # 2 -->   [1, 10, 20, 30, 40] 에서 0번 인덱스가 나온다. 하지만 정답은 1번 인덱스임 
    # 그렇기에 현재 인덱스값인 1 < 2이면 +1 한 1번 인덱스를 반환
    if li[st] >= num:
        return st
    else:
        return st + 1 

for i in range(1, n):
    if ma[i] > li[-1]:
        li.append(ma[i])
        dp.append(( len(li)-1, ma[i] ))
    
    else:
        idx = BS(ma[i])
        li[idx] = ma[i]
        dp.append((idx, ma[i]))
    

tmp = len(li) - 1 # LIS는 나왔음 유효한 지 체크 
ans = []

for i in range(len(dp)-1, -1, -1): # 앞에 있는 것들은 앞에 있을 가능성이 큼
    
    if dp[i][0] == tmp: # 가장 큰 수의 idx를 가지고 있는 것을 ans에 넣기
        ans.append(dp[i][1])
        tmp -= 1


print(len(li))
print(*ans[::-1])

    
