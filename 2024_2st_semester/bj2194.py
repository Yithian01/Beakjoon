# CCW를 활용해서 선분A, 선분B의 방향을 알아온다.
# (1) 선분A 기준 선분B의 양끝 점 2개 abc, abd
# (2) 선분B 기준 선분A의 양끝 점 2개 cda, cdb 

# 각 단계의 값을 곱해주었을 때 양쪽다 0인 경우는 다음과 같이 나타낼수 있다.
#   1) 모두 평행할 때 
#   2) 한쪽이 붙어있는 경우 
#   3) 평행하지만 붙어있지 않는 경우 
#   위 1, 2, 3을 가르기 위해서 다음 조건을 건다.
#   선분A에 가장 긴 위치의 좌표보다 선분B에 가장 짧은 좌표가 더 크다면 붙어있지 않은 평행임

# 그 이외에는 각 단계의 값을 곱해주었을 때 음수 or 0이 둘다 나오면 붙어있는 것이 확정이다.
# 확정 시 유니온 파인드를 통해 가장 작은 값으로 바꿔준다.

# 유니온 파인드한 결과를 출력한다.

# 시간 복잡도 계산: NC2 => N^2 => 3 * 10^3 => 9 * 10^6 정도
import sys
input = sys.stdin.readline

def FIND(x):
    if num[x] != x:
        return FIND(num[x])

    return x
    
def UNION(a, b):
    a = FIND(a)
    b = FIND(b)

    if a > b:
        a, b = b, a
    
    num[b] = a



def CCW(ar, ac, br, bc, cr, cc):
    return (br - ar) * (cc - ac) - (bc - ac) * (cr - ar)

def CHECK(i , j):
    ar ,ac, br, bc = ma[i]
    cr ,cc, dr, dc = ma[j]

    minAr, minAc = min(ar, br), min(ac, bc) # 선분A최소 r, c
    maxAr, maxAc = max(ar, br), max(ac, bc) # 선분A최대 r, c
    minBr, minBc = min(cr, dr), min(cc, dc) # 선분B최소 r, c
    maxBr, maxBc = max(cr, dr), max(cc, dc) # 선분B최대 r, c


    abc = CCW(ar, ac, br, bc, cr, cc)
    abd = CCW(ar, ac, br, bc, dr, dc)
    cda = CCW(cr, cc, dr, dc, ar, ac)
    cdb = CCW(cr, cc, dr, dc, br, bc)

    # 선분 A와 B의 모든 끝 점이 평행할때 
    if abc * abd == 0 and cda * cdb == 0:
        # A의 가장 작은 높이가  B의 가장 큰 높이보다 작아야 함 
        # B의 작은 높이가 A의 가장 큰 높이보다 작아야 함
        # A의 가장 작은 길이가 B의 가장 긴 길이보다 작아야 함
        # B의 가장 작은 길이가 A의 가장 긴 길이보다 작아야 함
        if minAr <= maxBr and minBr <= maxAr and minAc <= maxBc and minBc <= maxAc:
            return True
        
    else:
        # 각 선분을 대상으로 할때 True가 되는 경우의 수이다.
        # 1) A를 대상으로 c , d는 -1, 1 이렇게 되거나 하나가 0이되어야 함 
        # 2) 그러므로 0이거나 음수가 되면 그룹을 할 수 있다는 것
        if abc * abd <= 0 and cda * cdb <= 0:
            return True
    
    return False



n = int(input())
ma = [list(map(int, input().split())) for _ in range(n)]
num = [ _ for _ in range(n)]



for i in range(n-1):
    for j in range(i + 1, n):
        
        if CHECK(i, j):
            UNION(i, j)


cnt = 0
ans = [0] * (n)

for i in range(n):
    if i == num[i]:
        cnt += 1
    
    ans[FIND(i)] += 1

print(cnt)
print(max(ans))


