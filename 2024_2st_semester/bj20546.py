import sys
input = sys.stdin.readline


n = int(input())
ma = list(map(int, input().split()))

def convert(ca, st, price):
    return ca + st * price

jh_cash = n 
jh_st = 0
for i in ma:
    if jh_cash >= i:
        jh_st += jh_cash // i
        jh_cash %= i


sm_cash = n 
sm_st = 0
up, down = 1, 1
for i in range(1, 14):
    # 동일 시 하락 X, 상승 X 연속을 초기화?
    if ma[i-1] == ma[i]:
        up, down = 1, 1

    elif ma[i-1] > ma[i]: # 하락
        up = 0
        down += 1
    
    elif ma[i-1] < ma[i]: # 상승
        down = 0
        up += 1

    
    if down >= 3: # 3일째 하락 
        if sm_cash >= ma[i]:
            sm_st += sm_cash // ma[i]
            sm_cash %= ma[i]

    elif up >= 3: # 3일째 상승
        sm_cash += sm_st * ma[i]
        sm_st = 0


jh = convert(jh_cash, jh_st, ma[-1])
sm = convert(sm_cash, sm_st, ma[-1])
 
if jh == sm:
    print('SAMESAME')
elif jh > sm:
    print('BNP')
else:
    print('TIMING')
