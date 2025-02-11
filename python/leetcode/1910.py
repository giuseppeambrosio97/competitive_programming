class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        i = 0
        while True:
            if s[i:(i+m)] == part:
                s = s[:i] + s[i+m:]
                i = 0
            else:
                i += 1
            if i >= len(s):
                return s

    

if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    print(Solution().removeOccurrences(s, part))