from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """Brute force T(n1*n2)"""
        # r = 0
        # for n1 in nums1:
        #     for n2 in nums2:
        #         r ^= (n1^n2)
        # return r
        """O(n1+n2)"""
        r = 0
        n1, n2 = len(nums1) & 1, len(nums2) & 1
        if not n1 and not n2:
            return 0
        if n1:
            for i in range(len(nums2)):
                r ^= nums2[i]
        if n2:
            for i in range(len(nums1)):
                r ^= nums1[i]
        return r



