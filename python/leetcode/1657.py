import collections as cll

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        S(n1,n2) = O(n) for counter
        T(n) = O(n)
        """
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False
        
        cw1 = cll.Counter(word1)
        cw2 = cll.Counter(word2)

        if set(cw1) != set(cw2):
            return False

        for el1, el2, in zip(cw1.most_common(), cw2.most_common()):
            if el1[1] !=  el2[1]:
                return False
            
        return True
        



if __name__ == '__main__':
    print(Solution().closeStrings("cabbba", "abbccc"))