class Solution:
    def isPalindrome(self, s: str) -> bool:
        """S(n)=O(n)=T(n)."""
        # st = ""
        # for si in s:
        #     if si.isalnum():
        #         st += si.lower()
        # for i in range(len(st) // 2):
        #     if st[i] != st[len(st)-1-i]:
        #         return False
        # return True
        """O(n)=T(n), S(n)=O(1)"""
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r  and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    t = Solution().isPalindrome(s)
    print(t)