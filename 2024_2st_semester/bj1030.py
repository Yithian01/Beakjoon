import sys
input = sys.stdin.readline

s, n, k, sr, er, sc, ec = map(int, input().split())
# s초 일 때 
# (sr, sc) ~ (er, ec) 모습 출력 
# 1초마다 N만큼 커진다. ( N^t ) => N^0, N^1, N^2, N^3
#                                   1    3    9    27
# 최대 N = 8, s = 10       8^10 까지 필요 (2^3)^10 => 2^30 => 10^9 보다 적게 필요
# 모든 공간을 나타내기에는 128MB의 공간 복잡도가 말이 안된다.

