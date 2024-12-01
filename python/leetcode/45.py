from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # n = len(nums)
        # @lru_cache(maxsize=None)
        # def ft(i: int) -> int:
        #     if i >= n - 1:
        #         return 0
        #     if i + nums[i] >= n - 1:
        #         return 1
        #     a = math.inf
        #     for j in range(i+1, i+1+nums[i]):
        #         a = min(a, 1+ft(j))
        #     return a
        # return ft(0)
        """O(n)=T(n)."""
        n = len(nums)
        cjump = 0
        cend = 0
        farthest = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == cend:
                cjump += 1
                cend = farthest
            if cend >= n - 1:
                return cjump
        return 0
    
if __name__ == '__main__':
    l = Solution().jump([2,3,1,1,4])
    print(l)
            

