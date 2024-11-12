class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        best = 0
        dct = {}
        while r < len(s):
            while r < len(s) and dct.get(s[r], 0) == 0:
                dct[s[r]] = dct.get(s[r], 0) + 1
                best = max(best, r - l + 1)
                r += 1
            dct[s[l]] -= 1
            l += 1

        return best
                


if __name__ == '__main__':
    s = "abac"
    print(Solution().lengthOfLongestSubstring(s))