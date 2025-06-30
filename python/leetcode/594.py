from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
 
        best = 0
        for i in counter:
            if i + 1 in counter:
                best = max(best, counter[i]+counter[i+1])
        return best

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    print(Solution().findLHS(nums))