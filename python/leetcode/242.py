from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = Counter(s), Counter(t)

        for k,v in cs.items():
            if k not in ct or v != ct[k]:
                return False
            ct.pop(k)
            
        return len(ct) == 0