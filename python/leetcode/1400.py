from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)

        ## if we have less than k chars we cannot construct k different string for sure
        if n < k:
            return False
        
        ## if cnt_odd are the number of chars with odd occurrences have to construct at least cnt_odd palindrome strings
        cnt_odd = 0
        counter = Counter(s)
        for occ in counter.values():
            cnt_odd += occ & 1

        if cnt_odd > k:
            return False
        
        ## if cnt_odd are < k and n >= k we can construct for sure k different palindrome strings.
        ## WHY?
        ## For sure we can take k chars and build k palidrome strings with one chars, then we can extend those string
        ## with pair of chars (odd - 1 = even) until we finish the string
        return True
        



if __name__ == '__main__':
    s = "annabelle"
    k = 2
    Solution().canConstruct(s, k)