import sys
input = sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))
num = [0] * 10 # 아 종류 10이하네 


ans = 0
st, ed = 0, 0
kind = 0
while ed < n:
    
    num[ ma[ed]] += 1
    if num[ ma[ed]] == 1:
        kind += 1
    

    if kind > 2:
        num[ ma[st]] -= 1
        if num[ ma[st]] == 0:
            kind -= 1
        st += 1

    tmp = ed - st + 1
    ans = max(ans, tmp)
    ed += 1

print(ans)