import sys
input = sys.stdin.readline

''''
    1) 재배치 가능 ( 동일 해야 함)
    2) 두 단어의 [처음, 끝] 문자열을 동일해야 함
    3) 모음 제거 문자열은 동일해야 함 ( 모음 때문에 길이가 다르면 안됨 )
        [a, e, i, o, u] 

'''

mo = ['a', 'e', 'i', 'o', 'u']
n = int(input())
be = input().rstrip()
af = input().rstrip()

be_num = [0] * 26
af_num = [0] * 26
 
if (be[0] != af[0]) or (be[-1] != af[-1]):
    print('NO')
    exit(0)


tw = ['', '']


for i in range(1, n-1):
    
    a = ord(be[i]) - ord('a')
    be_num[a] += 1

    b = ord(af[i]) - ord('a')
    af_num[b] += 1

    if be[i] not in mo:
        tw[0] += be[i]

    if af[i] not in mo:
        tw[1] += af[i]


if (tw[0] == tw[1]):
    for i in range(26):
        if be_num[i] != af_num[i]:
            print('NO')
            break
    else:
        print('YES')

else:
    print('NO')