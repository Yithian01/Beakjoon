# D일 경우 최대 500만원까지 그 달에 충전할 수 있다. 
# 그러므로 이전달에 12만원을 현질 후 이번달에 D가능 최대금액은 500이다.
# DD 일 경우 다음 달도 또한 500을 현질 할 수 있다. 
import sys
input = sys.stdin.readline

n = int(input())
rank = list(map(int, input().split()))
res = input().rstrip()


table = {}
table['B'] = rank[0] -1 
table['S'] = rank[1] -1 
table['G'] = rank[2] -1 
table['P'] = rank[3] -1 
table['D'] = rank[3]

ans, be = 0, 0
for i in res:

    if i == 'D':
        ans += table[i]
        be =  table[i]
    else:
        ans += table[i] - be
        be = table[i] - be

print(ans)