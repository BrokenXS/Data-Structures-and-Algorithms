from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge(arr, L, M, R):
        print('ss', arr)
        left, right = arr[L : M + 1], arr[M + 1 : R + 1]
        print('cc', L ,R)
        print('aa', left ,right)
        i, j, k = L, 0, 0

        while j < len(left) and k < len(right):
            print(left[j] ,right[k] )
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1

    def mergeSort(arr, l, r):
        if l == r:
            return

        m = (l + r) // 2
        mergeSort(arr, l, m)
        # mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return

    mergeSort(nums, 0, len(nums))
    return nums
nums = [10,9,1,1,1,2,3,1]
sortArray(nums)