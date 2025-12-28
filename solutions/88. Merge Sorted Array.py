class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1.copy()[:m]
        n2 = nums2
        curr1, curr2, curr = 0, 0, 0
        while curr1 < m and curr2 < n:
            if n1[curr1] < n2[curr2]:
                nums1[curr] = n1[curr1]
                curr1 += 1
            else:
                nums1[curr] = n2[curr2]
                curr2 += 1
            curr += 1
        while curr1 < m:
            nums1[curr] = n1[curr1]
            curr1 += 1
            curr += 1
        while curr2 < n:
            nums1[curr] = n2[curr2]
            curr2 += 1
            curr += 1
