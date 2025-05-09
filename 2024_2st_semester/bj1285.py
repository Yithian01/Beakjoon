import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
    하나의 행, 열을 뒤집을 수 있음 
    각 단계의 경우의 수 => 2N , (N == M 이다.)
    최대 40번 -> 한 단계에

    bfs는 불가능 -> 2^400개의 저장상태를 VI에 저장해야 하는데 불가능 

    1) 비트 마스킹: 0 ~ 111까지 
        000, 001, 010, 011, 100, 101, 110, 111 <-- 각 열을 뒤집는 경우 
    
    2) 각 행을 뒤집는 경우 계산
        2중 for문 이용해 각 행의 T의 개수를 알아낸다.
        T를 이용해 H의 개수가 많은 경우로 만들어 준다. 

    3) 정답을 min을 이용해 계산 
    
    시간복잡도 계산: O( 2^20 * 20^2)
    2^20 = 10^6
    N^2 = 4 * 10^2 
    4 * 10^8 정도 4초정도
'''


n = int(input())
ma = [list(input().rstrip()) for _ in range(n)]
ans = INF

for bit in range(1 << n):
#   tmp = ma.copy() <-- 이거 얕은 카피, 딥카피 해야함
    tmp = [ma[i][:] for i in range(n)]    
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                tmp[i][j] = 'T' if tmp[i][j] == 'H' else 'H'

    res = 0
    for j in range(n):
        cnt = 0
        for i in range(n):
            if tmp[i][j] == 'T':
                cnt += 1
        
        res += min(cnt, n - cnt)
    
    ans = min(ans, res)

print(ans)