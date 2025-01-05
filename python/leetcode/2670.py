from collections import Counter, defaultdict
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        rcounter = Counter(nums)
        lcounter = defaultdict(int)

        res = []
        for i in range(len(nums)):
            rcounter[nums[i]] -= 1
            if rcounter[nums[i]] == 0:
                del rcounter[nums[i]]
            lcounter[nums[i]] += 1

            res.append(len(lcounter)-len(rcounter))


        return res


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    t = Solution().distinctDifferenceArray(nums)
    print(t)