from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)

        res = ""

        char_idx = 25
        while char_idx >= 0:
            ch = chr(char_idx + ord("a"))
            if cnt[ch] <= 0:
                char_idx -= 1
            else:
                resid = cnt[ch]
                use = min(resid, repeatLimit)
                res = res + ch * use
                cnt[ch] -= use

                if cnt[ch] > 0:
                    smaller_idx = char_idx - 1
                    while smaller_idx >= 0 and cnt[chr(smaller_idx + ord("a"))] <= 0:
                        smaller_idx -= 1
                    if smaller_idx < 0:
                        return res
                    
                    res = res + chr(smaller_idx + ord("a"))
                    cnt[chr(smaller_idx + ord("a"))] -= 1

        return res
            


if __name__ == "__main__":
    s = "ccccc"
    repeatLimit = 3
    t = Solution().repeatLimitedString(s, repeatLimit)
    print(t)
