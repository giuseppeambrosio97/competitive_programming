from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        res = 0

        old_n = len(chars)

        while l < old_n:
            count = 1
            r = l + 1
            while r < old_n and chars[r] == chars[l]:
                count += 1
                r += 1

            chars += [chars[l]]
            res += 1
            if count > 1:
                digits = list(str(count)) 
                chars += digits
                res += len(digits)            
            l = r
        
        del chars[:old_n]

        return res





if __name__ == '__main__':
    print(Solution().compress(["a","a","b","b","c","c","c"]))
        