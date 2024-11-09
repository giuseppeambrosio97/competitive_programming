from dataclasses import dataclass

@dataclass
class StackItem:
    min_: int
    val: int

class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            si = StackItem(
                val=val,
                min_=val,
            )
        else:
            si = StackItem(
                val=val,
                min_=min(self.s[-1].min_, val)
            )
        self.s.append(si)


    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1].val

    def getMin(self) -> int:
        return self.s[-1].min_