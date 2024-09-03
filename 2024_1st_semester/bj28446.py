import sys
input = sys.stdin.readline

# 1 x w : x에 w를 넣는다.
# 2 w : w가 있는 곳 출력

# 2번요청 시 무조건 존재


table = {}
for _ in range(int(input())):
    ma = list(map(int, input().split()))
    if len(ma) == 3:
        table[ ma[2] ] = ma[1]

    elif len(ma) == 2:
        print(table[ ma[1] ])


