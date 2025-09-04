from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge(arr, L, M, R):
        left, right = arr[L : M + 1], arr[M + 1 : R + 1]
        print(f"Merging: left={left}, right={right}, into arr[{L}:{R+1}]")
        i, j, k = L, 0, 0

        while j < len(left) and k < len(right):
            print(f"Comparing left[{j}]={left[j]} and right[{k}]={right[k]}")
            if left[j] <= right[k]:
                arr[i] = left[j]
                print(f"Placed {left[j]} at arr[{i}]")
                j += 1
            else:
                arr[i] = right[k]
                print(f"Placed {right[k]} at arr[{i}]")
                k += 1
            i += 1
        while j < len(left):
            arr[i] = left[j]
            print(f"Placed remaining left[{j}]={left[j]} at arr[{i}]")
            j += 1
            i += 1
        while k < len(right):
            arr[i] = right[k]
            print(f"Placed remaining right[{k}]={right[k]} at arr[{i}]")
            k += 1
            i += 1
        print(f"Result after merge: {arr[L:R+1]}")

    def mergeSort(arr, l, r):
        print(f"mergeSort called on arr[{l}:{r}] -> {arr[l:r]}")
        if l >= r:
            return
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        print(f"Array after sorting arr[{l}:{r}]: {arr[l:r+1]}")

    mergeSort(nums, 0, len(nums) - 1)
    print(f"Final sorted array: {nums}")
    return nums

nums = [10,9,1,1,1,2,3,1]
sortArray(nums)