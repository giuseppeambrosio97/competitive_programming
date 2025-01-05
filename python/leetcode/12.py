
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_mapping = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        res = []

        for value, symbol in roman_mapping:
            while num >= value:
                num -= value
                res.append(symbol)

        return "".join(res)


if __name__ == "__main__":
    num = 4000
    t = Solution().intToRoman(num)
    print(t)
