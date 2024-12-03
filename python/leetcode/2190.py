from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        i, j = 0, 0
        while i < len(s):
            if i == spaces[j]:
                res += " "
                j += 1
            else:
                res += s[i]
                i+=1
            if j >= len(spaces):
                return res + s[i:]    
        return res



if __name__ == '__main__':
    s = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    t = Solution().addSpaces(s, spaces)
    print(t)