from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        - k = 0:
            - count just the longest consecutive sequence of 1s

        - k > 0:
            - compute the array idxs_0[i] = index of nums in which there is the i-th 0s
            - iterate over the idxs_0 array like a sliding window: k at time
                - compute the solution value for each of this solution

        T(n,k) = O(n)
        S(n,k) = O(n)
        """
        if k == 0:
            j = 0
            best = 0
            while j < len(nums):
                count_1 = j
                while count_1 < len(nums) and nums[count_1] == 1:
                    count_1 += 1
                    best = max(best, count_1 - j)
                j = count_1 + 1

            return best

        idxs_0 = []
        for idx, el in enumerate(nums):
            if el == 0:
                idxs_0.append(idx)

        if len(idxs_0) <= k:
            return len(nums)
        
        if len(idxs_0) == len(nums):
            return k
                
        i = 0
        best = 0
        while i + k <= len(idxs_0):
            if i == 0:
                l = 0
            else:
                l = idxs_0[i] if idxs_0[i] - idxs_0[i-1] <= 1 else idxs_0[i-1]+1

            if i == len(idxs_0) - k:
                r = len(nums) - 1
            else:
                idx = max(i+k-1,0)
                r = idxs_0[idx] if idxs_0[min(i+k, len(idxs_0)-1)] - idxs_0[idx] <= 1 else idxs_0[i+k] - 1
            best = max(best, r-l+1)
            i += 1 

        return best


if __name__ == '__main__':
    nums = [0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
    # nums = [0,0,1,1,1,0,0]
    nums = [0,1,1,1,1,0,1,1]
    k = 1

    print(Solution().longestOnes(nums, k))