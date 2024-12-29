from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        s, p = 0, power
        l, r = 0, len(tokens) - 1

        while l <= r:
            ## try first always FU if not possible try FD if not possible end the loop
            if p >= tokens[l]:
                p -= tokens[l]
                s += 1
                l += 1
            elif s >= 1 and r-l+1 >= 2:
                p += tokens[r]
                s -= 1
                r -= 1
            else:
                return s
            
        return s


if __name__ == "__main__":
    tokens = [200,100]
    power = 150
    t = Solution().bagOfTokensScore(tokens, power)
    print(t)
