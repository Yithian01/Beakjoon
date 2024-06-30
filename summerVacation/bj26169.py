# NM => 25 밖에 되질 않는다. 못가는 부분의 캐싱을 해주어도 가능할 것 
# 최악의 경우 1step => 4방향 

#                    3
#                  3 2 3
#     1          3 2 1 2 3
#   1 0 1  =>  3 2 1 0 1 2 3
#     1          3 2 1 2 3
#                  3 2 3
#                    3

# 각스텝 당 재귀호출 횟수 : 4 * 3 * 3 => 36
import sys
input = sys.stdin.readline
dir = [(-1, 0),(0, -1),(1, 0),(0, 1)] # 북 서 남 동


def dfs(r, c, vi, cnt, step):
    if cnt >= 2:
        print(1)
        exit(0)

    if step >= 3:
        return 
    
    for dr, dc in dir:
        nr = r + dr 
        nc = c + dc

        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
            continue

        if ma[nr][nc] == -1:
            continue

        if not vi[nr][nc]:
            vi[nr][nc] = True
            dfs(nr, nc, vi, cnt + ma[nr][nc], step + 1)
            vi[nr][nc] = False
    

    return 

ma = [list(map(int, input().split()))for _ in range(5)]
n, m = map(int, input().split())

vi = [[False] * 5 for _ in range(5)]
vi[n][m] = True
dfs(n, m, vi, ma[n][m], 0)
print(0)