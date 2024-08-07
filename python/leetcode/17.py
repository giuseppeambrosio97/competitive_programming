from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" 
        }

        _n = len(digits)

        def _letterCombinations(i: int):
            if i == _n - 1:
                return list(mapping[digits[i]])
            r = _letterCombinations(i+1)

            rs = []
            for c in list(mapping[digits[i]]):
                for r_ in r:
                    rs.append(f"{c}{r_}")

            return rs
        
        if _n == 0:
            return []
        
        return _letterCombinations(0)
        

if __name__ == '__main__':
    digits = ""
    s = Solution().letterCombinations(digits=digits)
    print(s)