from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i]) 


        for i in range(len(nums)):
            if i == 0:
                lsum = 0
                rsum = prefix_sum[-1] - nums[0]
            else:
                lsum = prefix_sum[i-1] 
                rsum = prefix_sum[-1] - prefix_sum[i]

            if lsum == rsum:
                return i
        
        return -1

            
if __name__ == '__main__':
    print(Solution().pivotIndex([2,1,-1]))