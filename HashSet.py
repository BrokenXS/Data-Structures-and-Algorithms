from collections import defaultdict
from typing import List

nums = [2,20,4,10,3,4,5]
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longSet = 0
    print(numSet)
    for num in numSet:
        if (num -1) not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            
            longSet = max(length, longSet)
    print(longSet)
    return longSet
#longestConsecutive(nums)

nums2 = [5,5,1,1,1,5,5]
def majorityElement(nums: List[int]) -> int:
    count = defaultdict(int)
    getMaxCount = 0
    res = 0
    for num in nums:
        count[num] +=1
        if count[num] > getMaxCount:
            getMaxCount = count[num]
            res = num
    return res
#majorityElement(nums2)

def fourSum(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            print(count)
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                for k in range(j + 1, len(nums)):
                    count[nums[k]] -= 1
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if count[fourth] > 0:
                        res.append([nums[i], nums[j], nums[k], fourth])

                for k in range(j + 1, len(nums)):
                    count[nums[k]] += 1

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res
nums = [3,2,3,-3,1,0]
target = 3
print(fourSum(nums, target))