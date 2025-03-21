import sys
input = sys.stdin.readline

# 이분탐색으로 원하는 a보다 큰 지점 , b보다 작은 지점을 찾는다. <-- log N
# x <= 20    | TTTFF 
# x >= 60    | FFFTT

def BS(s, x):  # 이상, 이하
    st, ed = 0, n -1


    if s == 'U':  # 이상
        while st <= ed:
            mid = (st + ed) // 2
            if ma[mid] < x:  # 10 < 20, st를 올려야함
                st = mid + 1
            else:
                ed = mid - 1

    elif s == 'D':  # 이하
        while st <= ed:
            mid = (st + ed) // 2
            if ma[mid] <= x:  # 30 <= 60, ed = mid
                st = mid + 1
            else:
                ed = mid - 1

    return st


n, m = map(int, input().split())
ma = list(map(int, input().split()))
res = [list(map(int, input().split())) for _ in range(m)]
# 좌표 정렬
ma.sort()

for i in res:
    a, b = i
    if a > b:
        a, b = b, a
    
    aa = BS("U", a)  # a 이상인 좌표의 첫 번째 인덱스
    bb = BS("D", b)  # b 이하인 좌표의 마지막 인덱스

    ans = (bb - aa)  # 원래 정답
    print(ans)
