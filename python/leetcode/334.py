from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest, mid = float('+inf'), float('+inf')
        _n = len(nums)

        if _n < 2:
            return False

        for a in nums:
            if (a < smallest):
                smallest = a
            elif (smallest < a and a < mid):
                mid = a
            elif (mid < a):
                return True
        return False


if __name__ == '__main__':

    s = Solution()

    sol = s.increasingTriplet([1,2,3,4,5])
    print(sol)