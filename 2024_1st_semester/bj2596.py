# 시간복잡도 계산: 6 * 8 * n => 48n 정도

import sys
input = sys.stdin.readline


table, res = {}, {}
table['A'] = '000000'
table['B'] = '001111'
table['C'] = '010011'
table['D'] = '011100'
table['E'] = '100110'
table['F'] = '101001'
table['G'] = '110101'
table['H'] = '111010'


# 두 개의 암호를 받아서 cnt가 1일 때까지 그 문자 허용하는 함수 
def check(a):

    for k, v in table.items():
        cnt = 0

        for i in range(6):
            if a[i] != v[i]:
                cnt += 1

            if cnt >= 2:
                break

        if cnt <= 1:
            return k

    return -1        
    
    



n = int(input())
ma = input().rstrip()
ans = ''

for i in range(0, len(ma), 6):
    
    tmp = check(ma[i: i+6])
    if tmp == -1:
        print(i // 6 +1)
        exit(0)
    
    ans += tmp



print(ans)