from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        if there are k cons and 5 vocals -> you can expand if the next is a vocals
        if there are > k cons and 5 vocals -> you have to shrink the window (move l)
        if there are < k cons and 5 vocals -> you have to expand until you find the k-th cons
        if there are < k cons and < 5 vocals -> you have to expand until you find the k-th cons and 5 vocals

        """

        n = len(word)
        vocals_list = "aeiou"

        
        def atleastk(kp: int):
            cnt = defaultdict(int)
            vocals = 0
            cons = 0
            res = 0
            l = 0

            for r in range(n):
                if word[r] in vocals_list:
                    cnt[word[r]] += 1
                    if cnt[word[r]] == 1:
                        vocals += 1
                else:
                    cons += 1

                while cons >= kp and vocals == 5:
                    res += (n - r) # we can expand withouth checking the same window until the end of the string
                    if word[l] in vocals_list:
                        cnt[word[l]] -= 1
                        if cnt[word[l]] == 0:
                            vocals -= 1
                    else:
                        cons -= 1
                    l += 1

            return res
        
        return atleastk(k) - atleastk(k+1)
                


if __name__ == "__main__":
    word = "iqeaouqiq"
    k = 2
    print(Solution().countOfSubstrings(word, k))
