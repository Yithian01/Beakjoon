# AB = i => 0 ~ ma[0][0]  <-- Ab를 0 ~ 가능한 수까지 가정 
# Ac => ma[0][0] - Ab 
# Bc => ma[2][1] - Ac 
# Ba => ma[1][0] - Bc 
# Ca => ma[0][1] - Ba 
# Cb => ma[2][0] - Ca

# 시간복잡도 : O(6N)

import sys
input = sys.stdin.readline

n = int(input())
ma = [list(map(int, input().split()))for _ in range(3)]
for i in range( ma[0][0] + 1):
    Ab = i 
    Ac = ma[0][0] - Ab
    Bc = ma[2][1] - Ac
    Ba = ma[1][0] - Bc
    Ca = ma[0][1] - Ba
    Cb = ma[2][0] - Ca

    if (Ab >= 0) and ( Ac >= 0) and ( Ba >= 0 ) and (Bc >=0) and (Ca >= 0 ) and ( Cb >= 0 ):
        print(1) 
        print(Ab, Ac , sep=' ')
        print(Ba, Bc , sep=' ')
        print(Ca, Cb , sep=' ')
        exit(0)

else:
    print(0)