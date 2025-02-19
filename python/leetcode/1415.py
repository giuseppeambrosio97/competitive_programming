from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        C = ["a", "b", "c"]
        cnt = [0]

        def bk(s: List[str]):
            if len(s) == n:
                cnt[0] += 1
                if cnt[0] == k:
                    return s
                return 

            for i in C:
                if s and s[-1] == i:
                    continue
                s.append(i)
                r = bk(s)
                if r:
                    return r
                s.pop()

        r = bk([])

        if not r:
            return ""

        return "".join(map(str, r))

if __name__ == "__main__":
    n = 1
    k = 4
    print(Solution().getHappyString(n,k))