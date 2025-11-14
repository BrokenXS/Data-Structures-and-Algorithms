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
    
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l: r + 1]
    

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