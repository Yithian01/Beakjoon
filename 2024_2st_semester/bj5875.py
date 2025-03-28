import sys
input = sys.stdin.readline
# 무조건 오타는 한개라면 나올 수 있는 경우의 수는 -2, 2라고할 수 있다.

# '(' = 1 
# ')' = -1

# (1) 닫는 것이 많을 경우 -2  
#    (1-1) -1인 경우가 ')'이므로 이 경우 '('로 바꾸어 주면 해결 ans +=1
#    (1-2) dp에 누적합이 -1이 될 경우 이제 두개 이상을 바꿔야 해결가능하므로 break
# 
# (2) 여는 것이 많을 경우 2    ||  ((((())) = [1,1,1,1,1,1,-1,-1,-1] 이런 경우와
#                                   한개만 틀려야 하기 때문에 앞에 ))))((())) 이런경우 불가능
#    (2-1) 1인 경우가 '(' 이므로 ans +=1 
#    (2-2) dp의 누적합이  

# 시간복잡도 계산 : O(N)
s = input().rstrip()
ss = []

for i in s:
    if i == '(':
        ss.append(1)

    else:
        ss.append(-1)

cnt = sum(ss)
ans = 0
dp = []

if cnt == -2: # ( )) 같이 닫는 괄호가 더 많은 경우
    dp.append(ss[0])
    for i in range(1, len(ss)):
        dp.append( dp[i-1] + ss[i] ) 
        if ss[i] == -1: # 
            ans += 1

        if dp[i] == -1: # 누적합이 -1이 되는 경우 이후는 올바르지 않다.
            break       # 우리는 한개만 바꿔줘야 하기 때문에 나간다.

elif cnt == 2: # 여는 것이 많다면 
    dp.append(ss[-1])
    for i in range(1, len(ss)):
        dp.append( dp[i-1] + ss[-1-i] ) 
        if ss[-1 -i] == 1: # 반대로 누적합을 해주어 1이 될때까지 반복
            ans += 1

        if dp[i] == 1: # 누적합이 -1이 되는 경우 이후는 올바르지 않다.
            break       # 우리는 한개만 바꿔줘야 하기 때문에 나간다.

    
print(ans)