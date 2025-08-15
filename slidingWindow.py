from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()
    l = 0
    for r in range(len(nums)) :
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False
    
nums = [1,2,3,1]
k = 3
#print(containsNearbyDuplicate(nums, k))

prices = [10,1,5,6,7,1]
def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = profit
        else:
            l = r
        r += 1
    print(maxP)       
    return maxP

def lengthOfLongestSubstring(s: str) -> int:
    window = set()
    l = 0
    res = 0
    for r in range(len(s)) :
        while s[r] in window:
            print('left',l)
            print('aaa',r, s[r])
            print('bbb',s[l])
            print(window)
            window.remove(s[l])
            l += 1
            
        window.add(s[r])
        print(window)
        res = max(res, len(window))
    
    return res
        
lengthOfLongestSubstring("zxyyyzz")
#maxProfit(prices)