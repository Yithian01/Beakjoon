# N^2인 LIS dp는 사용 불가능 
# 빈 배열 dp를 만들어서 ma[0]를 처음에 넣어준다.
# 이후 ma에 값을 배열에 있는 값과 비교한다.
# 오름차순이므로 dp의 마지막 -1번째 index와 비교해서 크다면 dp에 넣어주기
# 같거나 작다면 현재 dp에서 들어갈 수 있는 가장  왼쪽을 찾는다.
# 그 위치의 값을 변경해준다.

# 시간 복잡도 계산: O(N * LOG K)
# 10^6 * 20 => 2 * 10^7정도
import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))
dp = [ma[0]]

def BS(e):
    st, ed = -1, len(dp) -1
    # TTTFFFF 가장 왼쪽의 F를 찾는 것이므로 ( ] 으로 설정

    while st <  ed -1:
        mid = (st + ed) // 2
        
        if dp[mid] < e:
            st = mid
        else:
            ed = mid

    return ed


for i in ma:
    if dp[-1] < i:
        dp.append(i)
    else:
        idx = BS(i)
        dp[idx] = i
    
print(len(dp))