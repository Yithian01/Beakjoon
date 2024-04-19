# (1) 메뉴를 dictionary에 저장 
# (2) 각 메뉴를 종류별로 일반 = 가격 총합
#                        특별 = 가격 총합
#                        서비스 = 갯수

# (3) 특별메뉴 가격이 0보다 클 때 일반 가격 총합을 체크 
# (4) 서비스 갯수가 1보다 크면 No
# (5) 서비스 갯수가 1일때 일반 + 특별 가격을 체크

# 시간 복잡도 게산 : 2A + B + C => O(N)
import sys
input = sys.stdin.readline

# 일반 => X
# 특별 => 일반 >= 20000
# 서비스 => 일+특 >= 50000
food = {}
A, B, C = map(int,input().split())
while A > 0:
    A -= 1
    k, v = map(str ,input().rstrip().split())
    food[k] = ["A", int(v)]
while B > 0:
    B -= 1
    k, v = map(str ,input().rstrip().split())
    food[k] = ["B", int(v)]
while C > 0:
    C -= 1
    k = input().rstrip()
    food[k] = ["C", 0]

no, sp, se = 0, 0, 0

for _ in range(int(input())):
    s = input().rstrip()
    if food[s][0] == 'A':
        no += food[s][1]
    elif food[s][0] =='B':
        sp += food[s][1]
    elif food[s][0] == 'C':
        se += 1


price = 0
if sp > 0 and no < 20000:
    print("No")
    exit(0)

price = no + sp
if se > 0 and price < 50000 or se > 1:
    print("No")
    exit(0)

print("Okay")