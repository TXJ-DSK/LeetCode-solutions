import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def three_way_quick_sort(left: int, right: int) -> None:
            if left >= right:
                return None
            pivot = nums[random.randint(left, right)]
            # i: boundary of elements < pivot (starts before left)
            # j: boundary of elements > pivot (starts after right)
            # k: current element being examined
            i = left - 1
            j = right + 1
            k = left
            while k < j:
                if nums[k] < pivot:
                    i += 1
                    swap(i, k)
                    k += 1
                elif nums[k] > pivot:
                    j -= 1
                    swap(j, k)
                    # not increment k, swapped element need to be examined
                else: # k-th element equals pivot element
                    k += 1
            three_way_quick_sort(left, i)
            three_way_quick_sort(j, right)
        three_way_quick_sort(0, len(nums) - 1)
        return nums
        
