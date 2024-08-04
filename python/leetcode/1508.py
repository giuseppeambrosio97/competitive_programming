from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod_ = (1e9 + 7)
        if len(nums) == 1:
            return nums[1] % mod_

        prefix_sum = []

        for num in nums:
            if len(prefix_sum) == 0:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[-1] + num)

        for i in range(1, len(nums)):
            prefix_sum_i = []
            for j in range(i, len(nums)):
                prefix_sum_i.append(prefix_sum[j]-prefix_sum[i-1])
            prefix_sum += prefix_sum_i
        
        sorted_sums = sorted(prefix_sum)

        return int(sum(sorted_sums[(left-1):(right)]) % mod_)


if __name__ == '__main__':
    s = Solution().rangeSum(nums=[1,2,3,4],n=4,left=1,right=10)
    print(s)