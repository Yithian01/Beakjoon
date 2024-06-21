import sys
input = sys.stdin.readline

sub = { "kor": 0, "eng": 1, "math":  2, "-": 3 }
fu = {'apple' : 0, 'pear' : 1, 'orange': 2, "-" :3  }
co = { 'red': 0, 'blue':1, 'green' :2, "-": 3 }



n , m = map(int, input().split())
ma = [[[0] * 4 for _ in range(4)] for _ in range(4)]


for _ in range(n):
    a, b, c = map(str, input().rstrip().split())
    
    ca = sub[a]
    cb = fu[b]
    cc = co[c]

    
    ma[ca][cb][cc] += 1


ma[3][3][3] = n
for i in range(3):
    for j in range(3):
        for k in range(3):
            ma[3][j][k] += ma[i][j][k]
            ma[i][3][k] += ma[i][j][k]
            ma[i][j][3] += ma[i][j][k]

            ma[3][3][k] += ma[i][j][k]
            ma[3][j][3] += ma[i][j][k]
            ma[i][3][3] += ma[i][j][k]
            
            
            


for _ in range(m):
    a, b, c = map(str, input().rstrip().split())

    ca = sub[a]
    cb = fu[b]
    cc = co[c]

    
    print(ma[ca][cb][cc])
