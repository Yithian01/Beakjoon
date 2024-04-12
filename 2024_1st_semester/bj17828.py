# 26 * n => 최대 
import sys
input = sys.stdin.readline
ma = {}

for i in range(26):
    tmp = 65 + i
    tmp = chr(tmp)
    ma[tmp] = i+1



n, m = map(int, input().split())
if 26 * n < m or m - n < 0 : continue





