from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        # at each iteration last_1_set at position j have the idx of the first number such that nums[idx] have the 
        # j-th bit set to 1
        last_1_set = [-1] * 31 # 31 -> because nums[i] <= 10**9
        for i in range(N-1,-1,-1):
            j = i
            for p in range(31):
                if nums[i] & (1 << p):
                    last_1_set[p] = i
                elif last_1_set[p] != -1:
                    j = max(j, last_1_set[p])
            res[i] = j-i+1
        return res



if __name__ == "__main__":
    nums = [1,0,2,1,3]
    print(Solution().smallestSubarrays(nums))