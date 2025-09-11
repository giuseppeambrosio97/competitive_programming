class Solution:
    def sortVowels(self, s: str) -> str:
        vocs = {"a", "e", "i", "o", "u"}
        vo = sorted([ord(si) for si in s if si.lower() in vocs], reverse=False)

        vi = 0
        t = []
        for si in s:
            if si.lower() not in vocs:
                t.append(si)
            else:
                t.append(chr(vo[vi]))
                vi+=1
        return "".join(t)
        


if __name__ == "__main__":
    s = "lYmpH"
    print(Solution().sortVowels(s))