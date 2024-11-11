class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nh, nn = len(haystack), len(needle)
        l, r = 0, 0

        if nh < nn:
            return -1

        while l < nh and l <= nh - nn:
            if haystack[l] == needle[r]:
                while l + r < nh and r < nn and haystack[l + r] == needle[r]:
                    r += 1
                if r == nn:
                    return l
            l += 1
            r = 0
        
        return -1


if __name__ == "__main__":
    haystack = "mississippi"
    needle = "issip"
    s = Solution().strStr(haystack, needle)
    print(s)
