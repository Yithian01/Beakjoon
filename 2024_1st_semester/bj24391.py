# 유니온 파인드 => 같은 그룹인지 확인하는 알고리즘
# 1) 배열의 index와 같은 같은 가진 배열을 생성
#         ㄴ> index : node 
#             value : 노드의 부모 노드
# 2) s, e 노드가 들어오면 둘의 부모 노드를 찾는다. 
#    index와 안의 값이 같을 때까지 반복해서 부모를 찾는다.
# 3) s, e의 부모 노드 중 작은 값을 큰 노드에 넣는다.
# 4) 그리고 이후 연결되었는지를 찾는데 한번 더 초기화 해야 한다. 
#    1 - 4 는 연결 되었는데, 5 - 4 를 연결 했다면 1 - 5 의 연결을 확인해주어야 하기 때문
 
# 시간 복잡도 계산 :  s,e를 연결하는 데 O(1)이 든다.  n = 10^5이므로 O(N) 이다.
import sys
input = sys.stdin.readline

def find(x):
    if x != ma[x]:
        ma[x] = find(ma[x])
    
    return ma[x]


def uf(s, e):
    s = find(s)
    e = find(e)

    if s > e:
        ma[s] = e
    else:
        ma[e] = s

n, m = map(int ,input().split())
ma = [i for i in range(n+1)]

for _ in range(m): 
    s, e = map(int, input().split())
    uf(s,e)


num = list(map(int, input().split()))

be = find(num[0])
cnt = 0
for i in range(1, len(num)):
    tmp = find(num[i])
    if be != tmp:
        cnt += 1
        be = tmp

print(cnt)