# DFS와 비트마스킹을 합친 기법 
# n이 극도로 낮기에 가능하다. n = 16

# 비트마스킹 : 1번 선택 => 1
#              2번 선택 => 10
#             1, 2번 선택 =>  11

# 만약 1-3-4-5 순서대로 가고있다면 다음과 같이 dp에 저장된다.
#                (3, 11101) : ? => (3, 29) : ?  

# 시간복잡도 계산: n * 2^n =>   16 * 2^16 = >    2^16 > 10^6 이므로 10^7이하일 것
import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]


dp = {} # 저장할 배열 key(방문한 노드 개수, 비트마스킹) : val(현재까지의 거리)


def DFS(cn, vi):
    if vi == (1 << n) - 1:
        if ma[cn][0]:
            return ma[cn][0] 
        else:
            INF

    if (cn,vi) in dp:
        return dp[(cn,vi)]
    
    
    tmp = INF
    for nn in range(1, n):
        if ma[cn][nn] == 0 or vi & (1 << nn):
            continue

        nTmp = DFS(nn, vi | (1 << nn)) + ma[cn][nn]
        tmp = min(tmp, nTmp)
    
    dp[(cn,vi)] = tmp
    return tmp


print(DFS(0,1))