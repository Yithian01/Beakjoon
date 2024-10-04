import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))

if N == 1:
    print("권병장님, 중대장님이 찾으십니다")
    exit(0)
else:
    arr = list(map(int, input().split()))
    ans = 0 
    
    for i in range(N-1):

        if graph[i] <= ans < arr[i] + graph[i]:
            ans = arr[i] + graph[i]



    if ans >= graph[N-1]:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")