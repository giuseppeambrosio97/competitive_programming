class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        c = 0
        while r >= 0 and s[r] != " ":
            r -= 1
            c += 1
        return c
