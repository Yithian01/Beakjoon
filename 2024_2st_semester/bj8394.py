import sys
input = sys.stdin.readline


n = int(input())

fibo = [1] * (n+1)
fibo[0] = 1


for i in range(2, n+1):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 10

print(fibo[n])