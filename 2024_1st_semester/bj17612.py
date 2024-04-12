# 주소 : "https://www.acmicpc.net/problem/17612"
# 입장하는 카운터는 작은 순서대로 
# 퇴장하는 카운터는  큰 순서대로
# ans += ( id * 퇴장순서 )

# **  입장하는 순서와 퇴장하는 순서가 모순된다고 생각할 수 있다.
#     예를 들어 0, 1번 카운터가 동시에 나간다면  1번 0번으로 퇴장한다.
#     이후 비어있는 0, 1번 카운터 중에 0번부터 채워주어야한다.
#         ㄴ> 1번이 먼저 나가도 0,1번이 동시에 빠졌다고 간주한다. **

# (1) 최소힙 사용해서 가장 (작은 시간, 작은 카운터 번호)를 알아낸다.
# (2) (1)의 순서대로 (짧은 시간, 큰 인덱스, 현재 사람순서) 로 넣는다.

# 예시) 
# ID = [123, 21, 34, 56, 45, 723, 55, 13, 910, 73]
# WE = [  4,  5, 14,  1,  7,   5,  7,  5,  10,  3]

# cnt = [(0, 0), (0, 1), (0, 2)] => 처음 시간은 모두 0이고 카운터 번호는 0 ~ k-1이다.
# cash = [0, 0, 0] => 처음에 모든 계산대(캐셔)는 0이다.

# cnt를 최소힙으로 pop한다.
# 1) t, x = 0, 0
#    cash[0] = 0 + 4 => 0번째 사람은 4초가 걸리고 0번째 계산대에 있다.
#    q <= (4, -0, 0) ==> 걸리는 시간, 계산대 위치, 고객 위치
#    계산대 위치를 최소힙으로 구현하기 위해서 -를 곱해준다.

# 2) t, x = 0, 1
#    cash[1] = 0 + 5 
#    q <= (5, -1, 1)

# 3) t, x = 0, 2
#    cash[2] = 0 + 14
#    q <= (14, -2, 2)

# 4) t, x = 4, 0 
#    cash[0] = 4 + 1 
#    q <= (5, -0, 3)

# ... 이런식으로 cnt는 k개를 유지해가며 
#     1) 가장 빨리 끝나면서 
#     2) 계산대 번호가 작은 순서대로 넣는다.

# 출력하는 부분은 
#     1) 빨리 끝나면서 
#     2) 계산대 번호가 가장 큰 것대로 넣는다.

# 시간 복잡도 계산 : O(N log N) 정도 
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

cu = [] # 고객 ID
we = [] # 물건 개수(무게)
n, m = map(int,input().split())

for _ in range(n):
    k, v = map(int,input().split())
    cu.append(k)
    we.append(v)

cnt = [] # 2차원 배열 index 0 => 시간, 1 => 카운터 숫자 

for i in range(m):
    heappush(cnt , (0, i))

cash = [0] * m # 각 계산대의 시간

ans = 0
q = [] #퇴장 순서 배열
for i in range(n):
    t, x = heappop(cnt)
    cash[x] += we[i]
    heappush(cnt, (cash[x], x))
    heappush(q, (cash[x], -x, i))
    

for i in range(1, n+1):
    _, _, tmp = heappop(q)
    ans += (i * cu[tmp])

print(ans)