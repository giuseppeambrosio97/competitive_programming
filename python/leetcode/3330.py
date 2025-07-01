

class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        l = 0
        for r in range(len(word)):
            if word[r] == word[l] and l != r:
                res += 1
            else:
                l = r
        return res
    
if __name__ == "__main__":
    print(Solution().possibleStringCount("ere"))