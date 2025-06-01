class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Basically try every possible choice for the first child by deleting a priori not feasible solution (too few candies to the first child). Then find the lower and upper bound for the second child and for the third child due to the fact that the sum should be exactly n the choice is fixed.
        So basically the solution is sum the range for the second child given the choice of the first child.
        """
        ans = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
        return ans