from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N, cnt = len(nums), 0

        for i in range(1, N-1):
            if nums[i] == nums[i-1]:
                continue
            prev = i - 1
            while prev > 0 and nums[prev] == nums[i]:
                prev -= 1
            next_ = i + 1
            while next_ < N - 1 and nums[next_] == nums[i]:
                next_ += 1

            if prev >= 0 and next_ < N and (nums[i] > nums[prev] and nums[i] > nums[next_]) or (nums[i] < nums[prev] and nums[i] < nums[next_]):
                cnt += 1
        return cnt


if __name__ == "__main__":
    nums = [44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,40,40]
    print(Solution().countHillValley(nums))