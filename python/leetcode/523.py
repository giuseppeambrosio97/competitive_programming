from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        psum = 0
        for i, a in enumerate(nums):
            psum += a
            mod = psum % k
            if mod not in d:
                d[mod] = i
            elif i - d[mod] >= 2:
                return True
        return False
    
if __name__ == "__main__":
    nums = [23,2,4,6,6]
    k = 7
    print(Solution().checkSubarraySum(nums, k))