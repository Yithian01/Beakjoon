import sys
input = sys.stdin.readline
# 트리를 만들어라 
# 값이 정해져 있다면 배수로 만들어 준다.
# 0번 노드가 비율은 1로 고정해주면서 계산해준다.

# 시간복잡도 계산: O(NV) 정도
def gcd( a,b ):
    if a % b == 0:
        return b
    
    return gcd(b, a % b)


n = int(input())
ma = [[] for _ in range(n)]
num = [0] * n 
vi = [False] * n

cnt = 1
for _ in range(n - 1):
    a, b, c, d = map(int, input().split())
    gc = gcd(c,d)
    c //= gc
    d //= gc

    ma[a].append((b, c, d))
    ma[b].append((a, d, c))
    cnt *= (c*d) 

num[0] = cnt


def DFS(x):
    vi[x] = True
    for i in ma[x]:
        if not vi[i[0]]:
            num[i[0]] = num[x] * i[2] // i[1] 
            DFS(i[0])
            # a:b = 3:1 일 경우 b = 1/3 여기에 0번째 노드를 1의 비율로 설정해줄 것이므로 곱해준다.

DFS(0)


res = num[0]
for i in num:
    res = gcd(res, i)

for i in num:
    print( (i // res), end=' ')