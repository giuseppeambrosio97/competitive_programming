from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        count = defaultdict(list)

        for idx, si in enumerate(s):
            if si != "*":
                count[si].append(idx)
            else:
                for chi in range(26):
                    ch = chr(97+chi)
                    if len(count[ch]) > 0:
                        count[ch].pop()
                        break
        
        res = [0]*len(s)

        for ch, comp in count.items():
            for c in comp:
                res[c] = ch
        

        return "".join([c for c in res if c != 0])

if __name__ == "__main__":
    s = "aaabab**"
    print(Solution().clearStars(s))