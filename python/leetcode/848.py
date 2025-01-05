from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """T(n)=O(n), S(n)=O(n)"""
        # n = len(shifts)
        # suffixsum = [0]*(n+1)

        # for i in range(n-1, -1, -1):
        #     suffixsum[i] = suffixsum[i+1] + shifts[i]

        # def letter_shift(letter: str, shift: int):
        #     return chr(((ord(letter) - 97 + shift) % 26) + 97)

        # res = ""

        # for i in range(n):
        #     res += letter_shift(s[i], suffixsum[i])

        # return res
        """T(n)=O(n), S(n)=O(1)."""

        total_shift = sum(shifts)
        res = ""

        for i in range(len(shifts)):
            res += chr(((ord(s[i]) - 97 + total_shift) % 26) + 97)
            total_shift -= shifts[i]
        return res


if __name__ == '__main__':
    s = "aaa"
    shifts = [1,2,3]
    t = Solution().shiftingLetters(s, shifts)
    print(t)