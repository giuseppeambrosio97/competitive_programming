from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if i < n - 2 and nums[i] == 0:
                for j in range(3):
                    nums[i+j] ^= 1
                res += 1
            if i >= n - 2 and nums[i] == 0:
                return -1
        return res
    
if __name__ == "__main__":
    nums = [0,1,1,1]
    print(Solution().minOperations(nums))