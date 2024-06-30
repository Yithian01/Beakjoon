from itertools import combinations, product
from bisect import bisect_left

dice = [[1, 2, 3, 4, 5, 6],  # 0
        [3, 3, 3, 3, 4, 4],  # 1
        [1, 3, 3, 4, 4, 4],  # 2
        [1, 1, 4, 4, 5, 5]]  # 3

LEN = len(dice)
for oP in product(range(6), repeat=LEN // 2):
    
    a = sum( dice[i][j] for i, j in zip([2, 3],oP))
    print(f'{a}', end=', ')

