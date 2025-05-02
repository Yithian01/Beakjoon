import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
    
    N 일 동안  사용할 금액 계산 
    K원 인출 
    M번만 빼서 쓰기 <-- 사용가능하면 사용 or 넣고 다시 k원 인출 
    정확ㅎ M을 맞추기 위해 남은 금액 K 최소화 
    
    최소 금액 K를 구하라 


    이분 탐색??
    st = 0, ed = sum(ma) =>  (st, ed] 
    T T T T T T F F F F 이건 줄 알았는데 반대다 
    F F F F F F T T T T 이거였다.

    1) IF TMP >= I: TMP - I ELSE CNT +=1, TMP - I
    2) IF CNT >= M: ST = MID ELSE ED = MID
    

        
'''

n, m = map(int, input().split())
ma = [int(input()) for _ in range(n)]

st, ed =  1, sum(ma) + 1

while st + 1 < ed:
    mid = (st + ed) // 2
    tmp, cnt = 0, 0

    isDone = False

    for i in ma:
        if tmp < i:
            tmp = mid
            cnt += 1

        if tmp >= i:
            tmp -= i
        else:
            isDone = True
            break

    
    if isDone:
        st = mid
        continue


    if cnt > m:
        st = mid
    
    elif cnt <= m:
        ed = mid


print(ed)