import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if n1 == n2:
            return str1 if str1 == str2 else ""
        
        _gcd = math.gcd(n1, n2)

        if str1[:_gcd] != str2[:_gcd]:
            return ""
        
        if n1 > n2:
            max_str_ = str1
            min_str_ = str2
        else:
            max_str_ = str2
            min_str_ = str1

        if min_str_ != max_str_[:len(min_str_)]:
            return ""
        

        guessed_gcd = min_str_[:_gcd]

        i = 0
        while _gcd*i < len(min_str_):
            l = _gcd*i
            r = _gcd*(i+1)
            if min_str_[l:r] != guessed_gcd:
                return ""
            i += 1
        
        i = 0
        while (len(min_str_) + _gcd*i) < len(max_str_):
            l = len(min_str_) + _gcd*i
            r = len(min_str_) + _gcd*(i+1)
            if max_str_[l:r] != guessed_gcd:
                return ""
            i += 1

        return min_str_[:_gcd]

            
    
if __name__ == '__main__':
    print(Solution().gcdOfStrings("ABCABC", "ABC"))