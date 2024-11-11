from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dcts = {}
        for s in strs:
            mapps = [0]*26
            for si in s:
                mapps[ord(si)-97] += 1
            mapps = "-".join([str(ch) for ch in mapps])
            if mapps not in dcts:
                dcts[mapps] = []
            dcts[mapps].append(s)
        return [v for v in dcts.values()]


if __name__ == '__main__':
    strs = ["bdddddddddd","bbbbbbbbbbc"]
    print(Solution().groupAnagrams(strs))