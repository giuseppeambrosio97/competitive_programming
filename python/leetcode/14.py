from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, ns = 0, len(strs)

        while True:
            for j in range(ns):
                if i >= len(strs[j]):
                    return strs[0][:i]
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
                

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    t = Solution().longestCommonPrefix(strs)
    print(t)