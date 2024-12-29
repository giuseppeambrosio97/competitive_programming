
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dct = {}

        for si in s:
            if si in dct:
                return si
            dct[si] = 1
        