class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = 0

        while i < len(s) and not s[i].isnumeric() and s[i] not in ["+", "-"]:
            if s[i].isalpha() or s[i] == ".":
                return 0
            i += 1

        if i == len(s):
            return 0
        
        if s[i] in ["+", "-"] and (i + 1 >= len(s) or not s[i+1].isnumeric()):
            return 0
        
        j = i + 1
        while j < len(s) and s[j].isnumeric():
            j += 1

        res = int(s[i:j])

        if res <= 0:
            return max(res, -2**31)
        else:
            return min(res, 2**31-1)

if __name__ == '__main__':

    print(Solution().myAtoi(".1"))