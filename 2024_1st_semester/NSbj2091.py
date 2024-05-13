import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(money, cnt):
    if vi[money] >= cnt:
        return 
    
    if money == X:
        vi[money] = cnt 

        for i in range(4):
            ans[i] = used[i]

        return 

    vi[money] = cnt

    if coin[0] >=