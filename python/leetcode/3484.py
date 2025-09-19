
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        c, r = ord(cell[0])-65, int(cell[1:])-1
        self.rows[r][c] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell,0)

    def getValue(self, formula: str) -> int:
        args = formula[1:].split("+")

        res = 0

        for arg in args:
            if arg.isdigit():
                res += int(arg)
            else:
                c, r = ord(arg[0])-65, int(arg[1:])-1
                res += self.rows[r][c]
        return res


if __name__ == "__main__":
    
    calls = ["Spreadsheet","setCell","resetCell"]
    args = [[24],["B24",66688],["O15"]]
    ss = Spreadsheet(*args[0])

    for call, arg in zip(calls[1:], args[1:]):
        print(getattr(ss,call)(*arg))
