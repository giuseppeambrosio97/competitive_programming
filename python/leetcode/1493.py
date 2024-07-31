from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        idxs_0 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                idxs_0.append(i)

        if len(idxs_0) == len(nums):
            return 0

        if len(idxs_0) <= 1:
            return len(nums) - 1
        
        best = 0
        for i in range(len(idxs_0)):
            if i == 0:
                l = 0 if nums[0] == 1 else 1
            else:
                l = idxs_0[i-1] + 1 

            if i == len(idxs_0) - 1:
                r = len(nums) - 1 if nums[-1] == 1 else len(nums) - 2
            else:
                r = idxs_0[i+1] - 1
            
            if l == r:
                best = max(best, nums[r])
            else:
                best = max(best, r - l)

        return best

        

if __name__ == '__main__':
    nums = [1,1,0,1]
    print(Solution().longestSubarray(nums))