from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """T(n)=O(n+n), S(n)=(n)."""
        n = len(s)
        differ = [0]*(n+1)

        for shift in shifts:
            l,r,t = shift
            t = t or -1
            differ[l] += t
            differ[r+1] -= t

        res = ""
        shift = 0
        for i in range(n):
            shift += differ[i]
            res += chr((ord(s[i]) - 97 + shift) % 26 + 97)

        return res

if __name__ == '__main__':
    s = "dztz"
    shifts = [[0,0,0],[1,1,1]]
    res = Solution().shiftingLetters(s, shifts)
    print(res)