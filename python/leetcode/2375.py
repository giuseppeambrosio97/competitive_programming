from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """greedy+backtracking using bitmask to check number used solution T(n!), S(n)=n"""
        n = len(pattern)

        def bk(used: int, res: List[int], idx: int = 0):
            if len(res) == n + 1:
                return res

            for i in range(1, n + 2):
                if used & (1 << i):
                    continue
                if idx > 0 and (
                    (pattern[idx-1] == "D" and i > res[-1])
                    or (pattern[idx - 1] == "I" and i < res[-1])
                ):
                    continue

                res.append(i)
                r = bk(used | 1 << i, res, idx+1)
                if r:
                    return r
                ## undo move
                res.pop()

        return "".join(map(str, bk(0, [])))


if __name__ == "__main__":
    pattern = "IIIDIDDD"
    print(Solution().smallestNumber(pattern))
