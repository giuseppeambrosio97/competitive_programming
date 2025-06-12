from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        best = -1
        suffix_max = [-1]*N # suffix[i] <- max_j for j=i+1,..,n nums[j]
        for j in range(N-2,-2,-1):
            suffix_max[j] = max(suffix_max[j+1], nums[j+1])
            if suffix_max[j+1] > nums[j+1]:
                best = max(best, suffix_max[j+1]-nums[j+1])
        return best
    
if __name__ == "__main__":
    nums = [1,5,2,10]
    print(Solution().maximumDifference(nums))