from itertools import permutations
import sys
input = sys.stdin.readline
INF = 10 ** 7

'''
    최대 조각수는 7이라면 
    7! 정도? =>

    주어지는 수에서 소수의 개수를 찾는다.
    가장 작은 수 ~ 가장 큰수 (만들 수 있는 최대 7자리수 -> 10^7 * )
'''

num = [ _ for _ in range(INF + 1)]
for i in range(2, INF):
    if num[i] != i:
        continue

    tmp  = i * 2
    while tmp <= INF:
        num[tmp] = i
        tmp += i

num[0] = -1
num[1] = -1

for _ in range(int(input())):
    s = input().rstrip()

    ans = set()
    for i in range(1, len(s) + 1 ):
        for tmp in permutations(s, i):
            ss = ""
            
            for j in tmp:
                ss += j
            
            if num[int(ss)] == int(ss):
                ans.add(int(ss))


    print(len(ans)) 