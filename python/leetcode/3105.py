from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """O(n^2)"""
        # res = 1
        # n = len(nums)
        # for i in range(n-1):
        #     if nums[i] != nums[i+1]:
        #         sign = nums[i] > nums[i+1]
        #         length = 1
        #         for j in range(i,n-1):
        #             if (nums[j] > nums[j+1]) != sign or (nums[j] == nums[j+1]):
        #                 break
        #             length += 1
        #         res = max(res, length)
        # return res
        """O(n)"""
        n = len(nums)
        if n == 1:
            return 1
        incr, decr, res = 1,1,1

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                incr += 1
                decr = 1
            elif nums[i] < nums[i-1]:
                decr += 1
                incr = 1
            else:
                decr,incr = 1,1
            res = max(incr,decr, res)
        return res


    
    
        

