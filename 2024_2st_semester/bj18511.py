import sys
sys.setrecursionlimit(10**8 + 1)
input = sys.stdin.readline
# 시간복잡도 계산: O(K^9) 
# 3자리의 원소가 n의 길이만큼 재귀 가능 즉 O(3^9정도)

n, m = map(int, input().split())
ma = list(map(int, input().split()))
ma.sort(reverse=True)

ans = -1

def BT(cnt, tmp):
    global ans

    # 길이가 n을 초과하는 경우 더 이상 진행하지 않음
    if cnt > len(str(n)):
        return

    # 숫자가 하나라도 만들어졌다면
    if cnt > 0:  
        num = int(tmp)
        if num <= n:
            ans = max(ans, num)
    
    # 백트래킹: 숫자 하나씩 이어가기
    for i in ma:
        BT(cnt + 1, tmp + str(i))

BT(0, "")
print(ans)
