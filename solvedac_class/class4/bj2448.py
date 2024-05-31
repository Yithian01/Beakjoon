# 열은 2 * n - 1 => 3은 제일 아래 열이 5 
#                   6은 제일 아래 열이 11 
#                   12는 제일 아래 열이 25

# n이 3보다 크다면 3단계로 분열될 수 있다. 
# 제일 위에점 => 2 * n -1 // 2 <-- 정 중앙에 별을 기준으로 아래 별들이 가지는 좌표는?
# 제일 위에서 [r - 3][c - 3] 인 지점
# 제일 위에서 [r - 3][c + 3] 인 지점 

# 3의 배수로 n이 주어진다.
# n // 3으로 줄어들고 배수당 별을 3개를 찍는다.

# 한 세트 당 별은 8개를 찍는다.
# 시간 복잡도 계산 : n  // 3 * (3 * 8)
import sys
input = sys.stdin.readline

n = int(input())
ma = [[" "] * (2*n -1) for _ in range(n)]

def bf(r, c, n):
    if n == 3:
        ma[r][c] = "*"
        ma[r+1][c-1] = "*"
        ma[r+1][c+1] = "*"
        for i in range(5):
            ma[r+2][c - 2 + i] = "*"
        return
    
    nn = n // 2
    bf(r, c, nn)  # 0, 5, 3
    bf(r + nn, c - nn, nn) # 3, 2, 3
    bf(r + nn, c + nn, nn) # 3, 8, 3


bf(0, (2 * n -1) // 2, n)
for i in range(n):
    print(''.join(ma[i]))

