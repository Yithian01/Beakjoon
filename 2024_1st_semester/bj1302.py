#시간복잡도 계산: 10^3 * 5 * 10 + 10^3 log(5 *10) => O(NM)
import sys
input = sys.stdin.readline

ma = {} 

for i in range(int(input())):
    s = input().rstrip()
    if s not in ma:
        ma[s] = 0
    
    ma[s] += 1


q = sorted(ma.items() , key= lambda x : ( -x[1], x[0]))
print(q[0][0])