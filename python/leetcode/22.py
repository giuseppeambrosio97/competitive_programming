from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr: str, openl: int, openr: int):
            """
            curr parenthesis string candidate
            openl: # of open left parenthesis  (
            openr: # of open right parenthesis )
            """
            if openl == n and openr == n:
                res.append(curr)
                return

            if openl < n:
                backtrack(curr + "(", openl + 1, openr)
            if openl > openr:
                backtrack(curr + ")", openl, openr + 1)

        backtrack("", 0, 0)

        return res


if __name__ == "__main__":
    n = 3
    t = Solution().generateParenthesis(n)
    print(t)
