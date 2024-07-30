from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set = set(nums1)
        nums2set = set(nums2)

        r1 = nums1set - nums2set
        r2 = nums2set - nums1set

        return [list(r1), list(r2)]
    

if __name__ == '__main__':
    print(Solution().findDifference([1,2,3,3], [1,1,2,2]))