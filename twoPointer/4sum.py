
from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return
            print('len',len(nums) - k + 1)
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                print('k',k)
                print('quad',quad)
                print('nums',nums[i])
                print('target',target)
                print(target - nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res 
   
