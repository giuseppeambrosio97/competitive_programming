class Solution:
    def kthCharacter(self, k: int) -> str:
        next_ch = lambda ch: chr(97+((ord(ch)-97)+1)%26)
        s = "a"
        while len(s) < k:
            s += "".join(next_ch(si) for si in s)
        return s[k-1]

        
if __name__ == "__main__":

    print(Solution().kthCharacter(10))