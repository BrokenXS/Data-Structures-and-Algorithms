from typing import List


def subsetXORSum(nums: List[int]) -> int:
    def backtrack(index: int, currentXOR: int, subset: list) -> int:
        print(f"index={index}, currentXOR={currentXOR}, subset={subset}")
        if index == len(nums):
            print(f"  Reached end: subset={subset}, returning {currentXOR}")
            return currentXOR
        # Include the current number
        include = backtrack(index + 1, currentXOR ^ nums[index], subset + [nums[index]])
        print(f"  After include nums[{index}]={nums[index]}: include={include}, subset={subset + [nums[index]]}")
        # Exclude the current number
        exclude = backtrack(index + 1, currentXOR, subset)
        print(f"  After exclude nums[{index}]={nums[index]}: exclude={exclude}, subset={subset}")
        print(f"index={index}, currentXOR={currentXOR}, total={include + exclude}, subset={subset}")
        return include + exclude

    return backtrack(0, 0, [])

def subsets(nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index: int, subset: list) -> int:
            if index == len(nums):
                print(subset)
                res.append(subset)
                return
            # Include the current number
            backtrack(index + 1, subset + [nums[index]])
            # Exclude the current number
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res

print(subsets([3,1,1]))