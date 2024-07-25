class Solution:
    def reverseVowels(self, s: str) -> str:
        vocals = {"a", "e", "i", "o", "u"}
        
        sl = list(s)

        l = 0
        r = len(s) - 1

        while l < r:
            if sl[l].lower() in vocals:
                swapped_ = False
                while l < r and  (not swapped_):
                    if sl[r].lower() in vocals:
                        ## swap s[l] <-> s[r]
                        sl[l], sl[r] = sl[r], sl[l]
                        swapped_ = True
                    r -= 1
            l+=1

        return "".join(sl)

            


if __name__ == '__main__':
    s = Solution()

    ss = s.reverseVowels("hello")
    print(ss)