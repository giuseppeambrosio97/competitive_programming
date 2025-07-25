from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_ = max(nums)
        return max_ if max_ < 0 else sum({n for n in nums if n > 0})
    
if __name__ == "__main__":
    nums = [-4,9,2]
    print(Solution().maxSum(nums))