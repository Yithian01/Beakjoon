import sys
input = sys.stdin.readline
INF= 2e9

ss = input().rstrip()

cntM = 0
cntK = 0

ansMax, ansMin = '', ''
for i in ss:
    if i == 'K':
        cntK += 1
        ansMax += str(5 * (10 ** cntM))
        cntM = 0     
    else:
        cntM += 1


if cntM != 0:
    ansMax += ('1' * cntM)
    cntM = 0


cntK = 0
for i in ss:
    if i == 'K':
        cntK +=1
        if cntM != 0:
            ansMin += str(10**(cntM-1))
            cntM = 0
        ansMin += '5'

    else:
        cntM += 1

if cntM != 0:
    ansMin += str((10 ** (cntM-1)))
 

print(f'{int(ansMax)}')
print(f'{int(ansMin)}')