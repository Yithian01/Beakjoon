# 시간복잡도 계산 : O(n)
# 틀린이유 : 최대 범위값보다 작은 INF값을 초기값으로 설정해줬기에 실패
import sys
input = sys.stdin.readline
INF = 2e9

n = int(input())
ma = list(map(int, input().split()))


# 0보다 클 경우 : a < b  , b를 줄이기 
# 0보다 작을 경우 : a < b , a를 올리기 

st, ed = 0, n-1
diff = INF
ans = [0,0]
while st < ed:
    origin = ma[st] + ma[ed]
    mid = abs(origin)
    
    
    if diff > mid:
        diff = mid
        ans = [ma[st], ma[ed]]

        if mid == 0:
            break
        


    if origin > 0:
        ed -=1    
    else:
        st += 1


print(*ans)