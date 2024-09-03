# 시간복잡도 계산: 8 * 10 * 8 8 10 => 64 * 10^2 => 6 * 10^3

def row_check(r, num):
    for x in range(9):
        if num == ma[r][x]:
            return False
    
    return True

def col_check(c, num):
    for x in range(9):
        if num == ma[x][c]:
            return False
    return True


def ab_check(r,c, num):
    cc = (c // 3) * 3 
    cr = (r // 3) * 3
    for i in range(3):
        for j in range(3):
            if ma[cr + i][cc + j] == num:
                return False
    
    return True


def dfs(cnt):
    if cnt >= len(q):
        for i in range(9):
            print(''.join(map(str, ma[i])))
        
        exit()

    r, c = q[cnt]
    for i in range(1, 10):
        if row_check(r, i) and col_check(c, i) and ab_check(r,c, i):
            ma[r][c] = i
            dfs(cnt + 1)
            ma[r][c] = 0


q = []
ma = []
for i in range(9):
    tmp = list(map(int, input()))
    for idx, j in enumerate(tmp):
        if j == 0:
            q.append((i, idx))
    ma.append(tmp)

dfs(0)