class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     """Dummy version with int python conversion."""
    #     ai = int(a,2)
    #     bi = int(b,2)
    #     return bin(ai + bi)[2:]

    def addBinary(self, a: str, b: str) -> str:
        
        
        i = 1
        res = ""
        prevcarry = 0
        carry = 0
        while i <= len(a) or i <= len(b):
            ai = int(a[-i]) if i <= len(a) else 0
            bi = int(b[-i]) if i <= len(b) else 0
            ## compute ri
            ri = None
            if prevcarry == 0:
                ri = ai^bi
            else:
                ri = 1 if ai^bi == 0 else 0
            res = f"{ri}{res}"

            ## compute carry
            if prevcarry == 0:
                carry = ai & bi
            else:
                carry = ai | bi
            prevcarry = carry
            i += 1

        if carry == 1:
            res = f"1{res}"
        return res



if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a,b))