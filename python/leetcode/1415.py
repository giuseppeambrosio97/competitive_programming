from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        choices = ["a", "b", "c"]

        if 3*(2**(n-1)) < k:
            return ""

        cnt = 0
        def bk(s: List[str]):
            nonlocal cnt
            if len(s) == n:
                cnt += 1
                if cnt == k:
                    return s
                return []
            for i in choices:
                if s and s[-1] == i:
                    continue
                s.append(i)
                r = bk(s)
                if r:
                    return r
                s.pop()
        return "".join(map(str, bk([])))

if __name__ == "__main__":
    n = 1
    k = 4
    print(Solution().getHappyString(n,k))