import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Steps:
            - sort T(nlogn)
            - for each number find the index range that satisfies the fair conditions (if exists)
                for each number two binary search are performed one for the lowest and one for the highest
        """
        nums = sorted(nums)
        cnt = 0

        def get_lowest_id_greater_or_equal(x):
            if nums[-1] < x:
                return -1
            if nums[0] >= x:
                return 0
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (r + l) // 2
                if nums[m] >= x and nums[m - 1] < x:
                    return m
                if nums[m] < x:
                    l = m + 1
                else:
                    r = m
            return m

        def get_greater_id_less_or_equal(x):
            if nums[0] > x:
                return -1
            if nums[-1] <= x:
                return len(nums) - 1

            l, r = 0, len(nums) - 1
            while l < r:
                m = (r + l) // 2
                if nums[m] <= x and nums[m + 1] > x:
                    return m
                if nums[m] > x:
                    r = m
                else:
                    l = m + 1
            return m

        for i, n in enumerate(nums):
            l = get_lowest_id_greater_or_equal(lower-n)
            r = get_greater_id_less_or_equal(upper-n)
            if l != -1 and r != -1:
                if i < l or i > r:
                    cnt += max(0,r - l + 1)
                else:
                    cnt += max(0, r - l)
        return cnt // 2
    
        """Solution using bisect std lib."""
    # def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    #     nums.sort()
    #     res = 0
    #     for i in range(len(nums)):
    #         a = bisect.bisect_left(nums, lower-nums[i], lo=i+1)
    #         b = bisect.bisect_right(nums, upper-nums[i], lo=i+1) - 1
    #         if a <= b:
    #             res += (max(b-a+1,0))
    #     return res
        



if __name__ == "__main__":
    nums = [-3,-10,-9,-5,4,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000]
    lower = -10
    upper = 11
    s = Solution().countFairPairs(nums, lower, upper)
    print(s)
