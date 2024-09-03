import sys
input = sys.stdin.readline

cnt = 0
# 비트 마스킹과
# 1 << 9        
for _ in range(int(input())):
    cnt += 1
    ans = ''

    # 위-아래, 왼-오른, 3x3
    row, col, rAndC = [], [], []
    ma = [list(map(int, input().split())) for _ in range(9)]
    input()

    for j in range(9):
        tmp = 0
        for i in range(9):
            tmp |= (1 << (ma[i][j]-1)) 

        row.append(tmp) 
            
    for i in range(9):
        tmp = 0
        for j in range(9):
            tmp |= (1 << (ma[i][j]-1)) 

        col.append(tmp)        


    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):       
            tmp = 0

            for dr in range(3):
                for dc in range(3):
                    nr = i + dr 
                    nc = j + dc 

                    tmp |= 1<< (ma[nr][nc] -1)

            rAndC.append(tmp)

    for i in range(9):
        if row[i] != 511 or col[i] != 511 or rAndC[i] != 511:
            ans = 'INCORRECT'
            break
    else:
        ans = 'CORRECT'

    print(f'Case {cnt}: {ans}' )