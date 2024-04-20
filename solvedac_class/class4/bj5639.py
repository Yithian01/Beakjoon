# 전위방식을 주므로 0번째보다 커지는 곳( 왼쪽, 오른쪽 )분리시킨다.
# 50 30 24 5 28 45 98 52 60 이라면 
# 1) 50 => [30 24  5 28 45],  [98, 52, 60]

#     30 => [24, 5, 28], [45]
#     24 => [5, 28] 
    
# 2) (1)을 index로 나타낼 수 있다.

#     0 => [1 ~ 5] [6 ~ 8]        6 => [7,8]
#     1 => [2 ~ 4] [5]            7 => [8]
#     2 => [3] [4]                8 => X
#     3 => X                      7 => X
#     4 => X                      6 => X
#     2 => X
#     5 => X 
#     1 => X

# 3)  3-4-5-1-8-7-6-0
#     5-28-24-45-30-60-52-98-50

# 시간복잡도 계산: n log n 분할정복이므로 => O(nlogn) 
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


q = []
while True:
    try:
        q.append(int(input()))
    except:
        break



def post(st, ed):
    if st > ed:
        return 
    
    mid = ed + 1
    for i in range(st+1, ed+ 1):
        if q[st] < q[i]:
            mid = i
            break
    
    post(st+1, mid-1)
    post(mid, ed)
    print(q[st])


post(0,len(q)-1)