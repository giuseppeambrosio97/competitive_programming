import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        numsi = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(numsi)
        score = 0
        while numsi:
            n,i = heapq.heappop(numsi)
            if nums[i] > 0:
                score += n
                nums[i] = -1
                if i - 1 >= 0:
                    nums[i-1] = -1
                if i + 1 < len(nums):
                    nums[i+1] = -1
        
        return score



if __name__ == "__main__":
    nums = [2, 1, 3, 4, 5, 2]
    t = Solution().findScore(nums)
    print(t)
