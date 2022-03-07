#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int searchInsert_lowerbound(vector<int> &nums, int target)
    {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }

    int searchInsert(vector<int> &nums, int target)
    {
        int l = 0, r = nums.size() - 1;
        if (target < nums[l])
        {
            return 0;
        }
        if (target > nums[r])
        {
            return r + 1;
        }
        while (l < r)
        {
            int m = (l + r) / 2;
            if (nums[m] == target)
            {
                return m;
            }
            else if (nums[m] >= target)
            {
                if (nums[m - 1] < target)
                {
                    return m;
                }
                else
                {
                    r = m - 1;
                }
            }
            else
            {
                l = m + 1;
            }
        }
        return r;
    }
};