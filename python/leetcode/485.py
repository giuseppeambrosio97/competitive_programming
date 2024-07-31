from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        l = 0
        while l < len(nums):
            r = l
            currenct_count = 0
            while r < len(nums) and nums[r] == 1:
                currenct_count += 1
                r += 1
            best = max(best, currenct_count)
            l = r + 1

        return best
                

if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))