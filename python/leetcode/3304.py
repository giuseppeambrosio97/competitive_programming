class Solution:
    def kthCharacter(self, k: int) -> str:
        ss = "a"

        next_ch = lambda ch: chr(97+((ord(ch)-97)+1)%26)

        while len(ss) < k:
            rr = []
            for si in ss:
                rr.append(next_ch(si))
            ss += "".join(rr)
        
        return ss[k-1]

        
if __name__ == "__main__":

    print(Solution().kthCharacter(10))