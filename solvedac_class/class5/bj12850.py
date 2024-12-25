import sys
input = sys.stdin.readline
MOD = 1000000007
# 인접행열 곱을 하는 문제 + 분할정복
# 
# 분할 정복 : log n + 각 부분의 이동 가능횟수를 곱해서 ans배열에 담고 리턴
#  
# 시간복잡도 계산: ㅇ8^3 * log N => 




ma = [[0] * 8 for i in range(8)]

ma[0][1] = ma[0][2] = 1
ma[1][0] = ma[1][2] = ma[1][3] = 1
ma[2][0] = ma[2][1] = ma[2][3] = ma[2][4] = 1
ma[3][1] = ma[3][2] = ma[3][4] = ma[3][5] = 1
ma[4][2] = ma[4][3] = ma[4][5] = ma[4][7] = 1
ma[5][3] = ma[5][4] = ma[5][6] = 1
ma[6][5] = ma[6][7] = 1
ma[7][4] = ma[7][6] = 1



def mul(a, b):
    ans = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                ans[i][j] += a[i][k] * b[k][j]
            ans[i][j] %= MOD
    return ans

def sol(li, m):
    if m == 1:
        return li
    tmp = sol(li, m // 2)
    if m % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), li) 

n = int(input())
ans = sol(ma, n)
print(ans[0][0])