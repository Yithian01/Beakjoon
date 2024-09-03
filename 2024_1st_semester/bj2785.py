import sys
input =  sys.stdin.readline

n = int(input())
ma = list(map(int, input().split()))
ma.sort()

cnt = n # 현재 체인 갯수
ans = 0 # 합친 횟수, 여는 횟수는 치지 않는다.

for i in ma:
    if cnt <= 1: # 탈출 조건1 : 현재 체인 1개
        break


    if i >= (cnt - 1): # n=3 이고 4,5,6 일때는 이어 붙이는 것이 효율적
        ans += (cnt - 1)
        break

    elif i == 1: # 1개의 체인을 열어 2개를 연결하면  
        cnt -= 2 # 3 -> 1개가 될 수 있다.
        ans += 1 # 연결 횟수 +1
    
    else:
        cnt -= (i + 1)
        ans += i

print(ans)