# 배열을 정렬후 가운데를 가장 작은 0번 idx부터 시작한다.
# 만약 모든 수의 합의 절대값이 0보다 작다면 시작점을 올려주는 것이 이득일 것이다.
# 두 개의 점을 잡고 가장 0에 가까운 곳을 찾는다. 
# 그렇기에 n-2번만큼 반복한다.

#시간복잡도 계산: (N-2)log(N - 2)
import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))

ma.sort()
INF = 3e9

ans = []
# 양끝을 제외하기 때문에 n-2로 잡는다.
for i in range(n-2):
   
    st = i + 1
    ed = n -1
    while st < ed:
        tmp =  ma[i] + ma[st] + ma[ed]

        if abs(tmp) < INF:
            INF = abs(tmp)
            ans = [ma[i], ma[st], ma[ed]]
        
        if tmp < 0:
            st += 1
        elif tmp > 0:
            ed -= 1
        else:
            break

print( *ans )