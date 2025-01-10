from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        needed = defaultdict(int)
        for w in words:
            needed[w] += 1
        step = len(words[0])
        ns, nw  = len(s), len(words)
        res = []        
        for i in range(step):
            l, r = i, i
            counter = defaultdict(int)
            cnt = 0
            while r + step <= ns:
                w = s[r:r+step]
                r += step
                if w in needed:
                    counter[w] += 1
                    cnt += 1
                    while counter[w] > needed[w]:
                        counter[s[l:l+step]] -= 1
                        cnt -= 1
                        l += step
                    if cnt == nw:
                        res.append(l)
                else:
                    cnt = 0
                    counter = defaultdict(int)
                    l = r 
        return res




if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    t = Solution().findSubstring(s, words)
    print(t)