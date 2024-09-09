import sys
input = sys.stdin.readline

minus, plus, zero = [], [], 0
ans = 0

n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        zero += 1
    elif a == 1:
        ans += 1
    elif a >1 :
        plus.append(a)

    else:
        minus.append(a)

plus.sort(reverse=True)
minus.sort()

if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        ans += plus[i] * plus[i+1]

else:
    


    if len(plus) > 1:
        for i in range(0, len(plus)-1, 2):
            ans += plus[i] * plus[i+1]
    
    ans += plus[-1]


# 0과 음수 ㅇ
# 음수가 짝수라면 곱하는게 무조건 좋다.
if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        ans += minus[i] * minus[i+1]


else:
    # 홀수라면 0번 index값 제거
    if zero >= 1:
        if len(minus) >= 2:
            minus.pop(-1)
        
    
    if len(minus) >= 2:
        for i in range(0, len(minus)-1, 2):
            ans += minus[i] * minus[i+1]
        
        if zero <= 0:
            ans += minus[-1]
        
        



print(ans)