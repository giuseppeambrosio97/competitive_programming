class Solution:
    def romanToInt(self, s: str) -> int:
        dd = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        i = 0
        cnt = 0
        while i < len(s):
            if i+1 < len(s) and dd[s[i]] < dd[s[i+1]]:
                cnt +=  dd[s[i+1]] - dd[s[i]]
                i += 2
            else:
                cnt += dd[s[i]]
                i += 1
        return cnt


if __name__ == "__main__":
    s = "LVIII"
    t = Solution().romanToInt(s)
    print(t)
