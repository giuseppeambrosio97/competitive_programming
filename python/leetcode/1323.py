class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6","9",1))


if __name__ == "__main__":

    num = 69999
    print(Solution().maximum69Number(num) )