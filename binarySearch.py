import math
from typing import List

nums = [-1, 0, 2, 4, 6, 8]
target = 7


def search(nums: List[int], target: int) -> int:

    l, r = 0, len(nums)
    while l < r:
        m = l + ((r - l) // 2)
        if nums[m] >= target:
            r = m
            print(r)
        elif nums[m] < target:
            l = m + 1
            print("aaa", l)

    return l


def mySqrt(x: int) -> int:
    left, right = 1, x
    while left < right:
        m = left + ((right - left) // 2)
        if m * m > x:
            right = m - 1
        else:
            left = m + 1
    print(m)
    return m

def minEatingSpeed(piles: List[int], h: int) -> int:
    l , r = 1 , max(piles)
    res = r

    while l <= r:
        k = (l + r)//2
        hours = 0
        for p in piles:
            hours += p//k
            print(hours, k)
        if hours <= h:
            res = k
            r = k - 1
        else:
            l = k + 1    
    return res



matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    l, r = 0, ROWS * COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        row, col = m // COLS, m % COLS
        print(row, col)
        if target > matrix[row][col]:
            l = m + 1
        elif target < matrix[row][col]:
            r = m - 1
        else:
            return True
    return False

# searchMatrix(matrix, target)
# search(nums, target)
# mySqrt(9)
print(minEatingSpeed([1,4,3,2], 9))
