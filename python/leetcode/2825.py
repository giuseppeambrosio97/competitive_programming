class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def is_good(s1,s2):
            if s1 == s2:
                return True
            _ord1 = ord(s1) - 97 
            _ord2 = ord(s2) - 97
            return ((_ord1 + 1) % 26) == _ord2
        j = 0
        for i, s1 in enumerate(str1):
            if is_good(s1,str2[j]):
                j += 1
            if j >= len(str2):
                return True
        print(j)
        return False
