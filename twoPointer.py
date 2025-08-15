from typing import List

def validPalindrome(s: str) -> bool:
        if s == s[::-1]:
            return True
        
        for i in range(len(s)):
            print(s[:i])
            print('sss',s[i + 1:])
            newS = s[:i] + s[i + 1:]
            print('aaaa',newS)
            print('cccc',newS[::-1])
            if newS == newS[::-1]:
                return True
        
        return False
    

def validPalindromeTwoPointer(s: str) -> bool:
    def is_palindrome(left: int, right: int) -> bool:
        print('aaaa',s[left])
        print('cccc',s[right])
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check by skipping one character either from the left or the right
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1
    return True

def mergeAlternately(word1: str, word2: str) -> str:

    result = []
    left = 0
    while left < min(len(word1), len(word2)):
        result.append(word1[left])
        result.append(word2[left])
        left += 1

    # Append the remaining characters
    result.append(word1[left:])
    result.append(word2[left:])
    print(result)
    return ''.join(result)    
     
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last = m + n - 1
    i, j = m - 1, n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
                
        last -= 1
    print(nums1)
    
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
                 
        

s = "abbadc"
word1 = "abc"
word2 = "xyz"
nums1 = [10,20,20,40,0,0]
m = 4
nums2 = [5,15]
n = 2
#merge(nums1,m,nums2,n)
#mergeAlternately(word1,word2)
#validPalindromeTwoPointer(s)
# result = validPalindrome(s)
print(fourSum([3,2,3,-3,1,0], 3))