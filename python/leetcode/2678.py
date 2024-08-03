from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def get_age(s: str) -> int:
            return int(s[11:13])
        
        return sum([1 for p in details if get_age(p) > 60])

if __name__ == '__main__':
    print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))