class Solution:
    def maxDiff(self, num: int) -> int:
        ns = str(num)
        first = ns[0]

        def get_max():
            if first != '9':
                return int(ns.replace(first, '9'))
            i = 1
            while i < len(ns) and ns[i] == "9":
                i+=1
            return int(ns.replace(ns[i] if i < len(ns) else ns[i-1], '9'))
        
        def get_min():
            if first != '1':
                return int(ns.replace(first, '1'))
            i = 1
            while i < len(ns) and ns[i] in ['0', '1']:
                i+=1
            return int(ns.replace(ns[i], '0')) if i < len(ns) else num

        return get_max() - get_min()
    
if __name__ == "__main__":
    num = 111
    print(Solution().maxDiff(num))