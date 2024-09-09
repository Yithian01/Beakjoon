import sys
input = sys.stdin.readline
INF= 1e9

def check(lr, k): # 가야하는 곳, 현재위치
    if k == 0:
        if lr == 0:
            return 0
        
        else:
            return 2
    elif k == lr:
        return 1
    # 인접한곳 1 
    elif abs(k - lr) == 1 or abs(k - lr ) == 3:
        return 3
    else:
        return 4


move = list(map(int, input().split()))
move.pop() # 맨 뒤에는 0이기에 빼준다.
n = len(move)

if n == 0:
    print(0)
    exit()

dp = [[[INF for _ in range(5)]for _ in range(5)] for _ in range(n+1)]    