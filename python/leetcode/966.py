import re
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask_voc(s: str) -> str:
            return re.sub(r"[aeiou]","*",s.lower())

        exact_m = set(wordlist)
        case_m = {}
        voc_m = {}

        for w in wordlist:
            wl = w.lower()
            case_m.setdefault(wl,w)
            voc_m.setdefault(mask_voc(wl),w)

        def findq(q:str)->str:
            if q in exact_m:
                return q
            if q.lower() in case_m:
                return case_m[q.lower()]
            if mask_voc(q) in voc_m:
                return voc_m[mask_voc(q)]            
            return ""

        return list(map(findq,queries))

if __name__ == "__main__":
    w = ["KiTe","kite","hare","Hare"]
    q = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    print(Solution().spellchecker(w,q))