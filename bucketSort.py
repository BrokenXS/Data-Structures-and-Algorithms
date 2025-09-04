from typing import List


def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        print(count)
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                print('count:', count)
                nums[index] = i
                print('index:', index)
                print('value:', nums[index])
                index += 1

sortColors([2,0,2,1,1,0])
