import sys
import copy
input = sys.stdin.readline
# 상하좌우의 이동 함수를 만들어준다.
# 상: i = 0, j = 현재
# 하: i = n-1, j = 현재 
# 좌 : i = 현재, j = 0
# 우 : i = 현재, j = n-1

# 시간 복잡도 계산: 2* 10^2^5 =>  2 * 10^7 정도

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def left_move(ma):
    for i in range(n):
        cur = 0
        for j in range(1, n):
            if ma[i][j] != 0:
                tmp = ma[i][j]
                ma[i][j] = 0
            
                if ma[i][cur] == 0:
                    ma[i][cur] = tmp
                elif ma[i][cur] == tmp:
                    ma[i][cur] *= 2
                    cur += 1
                else:
                    cur += 1
                    ma[i][cur] = tmp

    return ma

def right_move(ma):
    for i in range(n):
        cur = n-1
        for j in range(n-1, -1, -1):
            if ma[i][j] != 0:
                tmp = ma[i][j] 
                ma[i][j] = 0 

                if ma[i][cur] == 0:
                    ma[i][cur] = tmp

                elif ma[i][cur] == tmp:
                    ma[i][cur] *= 2
                    cur -= 1
                
                else:
                    cur -= 1
                    ma[i][cur] = tmp

    return ma

def up_move(ma):
    for j in range(n):
        cur = 0
        for i in range(n):
            if ma[i][j] != 0:
                tmp = ma[i][j] 
                ma[i][j] = 0 

                if ma[cur][j] == 0:
                    ma[cur][j] = tmp 

                elif ma[cur][j] == tmp:
                    ma[cur][j] *= 2
                    cur += 1
                
                else:
                    cur += 1
                    ma[cur][j] = tmp 

    return ma


def down_move(ma):
    for j in range(n):
        cur = n-1 
        for i in range(n-1, -1, -1):
            if ma[i][j] != 0:
                tmp = ma[i][j]
                ma[i][j] = 0

                if ma[cur][j] == 0:
                    ma[cur][j] = tmp 

                elif ma[cur][j] == tmp:
                    ma[cur][j] *= 2
                    cur -= 1
                
                else:
                    cur -= 1
                    ma[cur][j] = tmp
    
    return ma

def dfs(cnt, ma):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if ma[i][j] > ans:
                    ans = ma[i][j]
        return
    
    for i in range(4):
        copy_list = copy.deepcopy(ma)
        if i == 0:
            dfs(cnt+1, left_move(copy_list))
        elif i == 1:
            dfs(cnt+1, right_move(copy_list))
        elif i == 2:
            dfs(cnt+1, up_move(copy_list))
        else:
            dfs(cnt+1, down_move(copy_list))


dfs(0, li)
print(ans)