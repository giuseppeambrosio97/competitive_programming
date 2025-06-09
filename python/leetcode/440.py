class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr: int, currpp: int):
            ## number rooted in the subtree with prefix curr
            steps = 0
            while curr <= n:
                steps += min(n+1,currpp) - curr
                curr *= 10
                currpp *= 10
            return steps
        curr = 1
        k -= 1
        while k > 0:
            step = count_steps(curr, curr+1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr

