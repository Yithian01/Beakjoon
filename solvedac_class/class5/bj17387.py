import sys
input = sys.stdin.readline

def CCW(ar, ac, br, bc, cr, cc):
    return (br - ar) * (cc - ac) - (cr- ar) * (bc - ac)


ma = [list(map(int, input().split())) for _ in range(2)]
a = ma[0][0:2]
b = ma[0][2:]
c = ma[1][0:2]
d = ma[1][2:]

a, b = sorted([a,b])
c, d = sorted([c,d])

abc = CCW(a[0], a[1], b[0], b[1], c[0], c[1])
abd = CCW(a[0], a[1], b[0], b[1], d[0], d[1])
cda = CCW(c[0], c[1], d[0], d[1], a[0], a[1])
cdb = CCW(c[0], c[1], d[0], d[1], b[0], b[1])

ar_max, ac_max = max(a[0], b[0]), max(a[1], b[1])
ar_min, ac_min = min(a[0], b[0]), min(a[1], b[1])
br_max, bc_max = max(c[0], d[0]), max(c[1], d[1])
br_min, bc_min = min(c[0], d[0]), min(c[1], d[1])




if (abc * abd) == 0 and (cda * cdb) == 0:
    
    if ar_min <= br_max and br_min <= ar_max and ac_min <= bc_max and bc_min <= ac_max:
        print(1)
    else:
        print(0)

elif (abc * abd) <= 0 and (cda * cdb) <= 0 :
    print(1)
else:
    print(0)