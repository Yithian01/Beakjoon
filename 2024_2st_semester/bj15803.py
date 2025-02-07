import sys
input = sys.stdin.readline
# 0을 나누면 오류가 뜨는 것을 처리하는 것보다 곱해서 0인지 처리해보자

# 3개의 좌표 입력받기
ma = [tuple(map(int, input().split())) for _ in range(3)]

# 좌표를 정렬 (x 값 기준으로)
ma.sort()

# 교차 곱을 사용하여 기울기 비교
br = ma[1][1] - ma[0][1]  # y 차이
bc = ma[1][0] - ma[0][0]  # x 차이

ar = ma[2][1] - ma[1][1]  # y 차이
ac = ma[2][0] - ma[1][0]  # x 차이

# 기울기가 같은지 확인
if br * ac == ar * bc:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
