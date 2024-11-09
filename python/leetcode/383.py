from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rids = Counter(ransomNote)
        mids = Counter(magazine)

        for k,v in rids.items():
            if k not in mids or mids[k] < v:
                return False
            
        return True

    
if __name__ == '__main__':
    s = Solution().canConstruct(
        "aa",
        "aab",
    )
    print(s)