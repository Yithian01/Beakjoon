import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
ma = list(map(int, input().split())) # 각 처음 영상
node = list(map(int, input().split())) # 각 영상 바로 위 
