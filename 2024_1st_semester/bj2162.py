import sys
input = sys.stdin.readline

def FIND(x):
    if x == node[x]:
        return x
    
    return FIND(node[x])

def UNION(a, b):
    a = FIND(a)
    b = FIND(b)

    if a > b:
        a, b = b, a

    node[b] = a


def cross(k, v):
    a = (k[0], k[1])
    b = (k[2], k[3])
    c = (v[0], v[1])
    d = (v[2], v[3])

    if a > b:
        a, b = b, a
    
    if c > d :
        c, d = b, c

    ab = (b[0] - a[0], b[1] - a[1]) 
    ac = (c[0] - a[0], c[1] - a[1]) 
    ad = (d[0] - a[0], d[1] - a[1]) 


