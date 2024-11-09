from typing import List
# from collections import Counter

class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     """T(n)=O(n)=S(n)."""
    #     c = Counter(nums)
    #     return c.most_common()[0][0]
    def majorityElement(self, nums: List[int]) -> int:
        """T(n)=O(n), S(n)=O(1)."""
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res

if __name__ == '__main__':
    print(Solution().majorityElement([2,2,1,1,1,2,2]))