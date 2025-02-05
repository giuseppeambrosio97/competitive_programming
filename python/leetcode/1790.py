class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [(ch1, ch2) for ch1, ch2 in zip(s1, s2) if ch1 != ch2]
        return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])
