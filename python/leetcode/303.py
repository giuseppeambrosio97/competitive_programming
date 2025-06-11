from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for n in nums:
            self.prefix.append(self.prefix[-1]+n if self.prefix else n)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left-1] if left > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)