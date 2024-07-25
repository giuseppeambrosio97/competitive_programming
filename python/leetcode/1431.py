from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        return [(candy + extraCandies) >= max_ for candy in candies]

                

if __name__ == "__main__":
    s = Solution()

    print(s.kidsWithCandies([2,3,5,1,3], 3))