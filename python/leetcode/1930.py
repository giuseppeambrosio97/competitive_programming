class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """T(n)=O(26*(n+n+n+n)), S(n)=O(26)."""
        cnt = 0
        for i in range(97, 97+26):
            letter = chr(i)
            first, last = s.find(letter), s.rfind(letter)
            if first != last and first != -1 and last != -1:
                cnt += len(set(s[first+1:last]))
        return cnt

if __name__ == '__main__':
    s = "bbcbaba"
    t = Solution().countPalindromicSubsequence(s)
    print(t)