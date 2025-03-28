import sys
input = sys.stdin.readline
INF =  sys.maxsize
'''
    - 6명 팀 아니면 뺴주기
    - 4명 점수만 더하기 
    - 5번째 사람 등수 체크 
'''


for _ in range(int(input())):
    n = int(input())
    ma = list(map(int, input().split()))
    team = [0] * (max(ma) + 1) # 들어온 팀 명수
    lastCnt = [5] * (max(ma) + 1) # 팀 별 마지막 주자 등수
    last = [5] * (max(ma) + 1) # 팀 별 마지막 주자 등수
    
    for val in ma:
        team[val] += 1
    
    dp = []                 # dp = 쓸데없는 팀 뺀 들어온 순서
    for val in ma:
        if team[val] >= 6:
            dp.append(val)
    
    socreCnt = [4] * (max(ma) + 1) # 팀 당 4인까지
    socre = [0] * (max(ma) + 1) # 팀 별 점수 || score[3] -> 팀3의 점수
    for idx, val in enumerate(dp):
        lastCnt[val] -= 1
        if lastCnt[val] == 0:
            last[val] = idx+1
        
        socreCnt[val] -= 1
        if socreCnt[val] >= 0:
            socre[val] += idx + 1

    
    ans = [INF, 0]
    for idx, val in enumerate(socre): # 팀, 점수
        if val == 0:
            continue
        
        if ans[0] > val:
            ans = [val, idx]

        elif ans[0] == val and last[ans[1]] > last[idx]:
            ans = [val, idx]

    
    print(ans[1])