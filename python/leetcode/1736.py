class Solution:
    def maximumTime(self, time: str) -> str:
        first, second = time.split(":")

        def t(value, l1, l2):
            if value[0] == "?" and value[1] == "?":
                return f"{l1}{l2}"
            if value[0] != "?" and value[1] != "?":
                return f"{value[0]}{value[1]}"
            if value[0] == "?":
                if int(value[1]) <= l2:
                    return f"{l1}{value[1]}"
                else:
                    return f"{(l1-1)}{value[1]}"
            if int(value[0]) == l1:
                return f"{value[0]}{l2}"
            else:
                return f"{value[0]}9"

        return f"{t(first,2,3)}:{t(second,5,9)}"
                

if __name__ == "__main__":
    times = [
        "?9:03",
        # "0?:3?",
        # "1?:22",
        # "?4:03"
    ]
    print(Solution().maximumTime(times[0]))