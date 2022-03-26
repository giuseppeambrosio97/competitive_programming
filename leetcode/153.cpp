#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int findMin(vector<int> &nums)
    {

        int r = nums.size() - 1, l = 0, m = 0;

        while (l <= r)
        {

            if (nums[l] <= nums[r])
            {
                return nums[l];
            }
            m = l + (r - l) / 2;
            if (nums[l] > nums[m])
            {
                r = m;
            }
            else
            {
                l = m + 1;
            }
        }

        return -1;
    }

    int findMinv2(vector<int> &nums)
    {
        int r = nums.size() - 1, l = 0, m = 0, res = nums[0];

        while (l <= r)
        {
            if (nums[l] <= nums[r])
            {
                res = min(res, nums[l]);
                break;
            }

            m = l + (r - l) / 2;

            res = min(res, nums[m]);
            if (nums[l] > nums[m])
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }

        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> v({2, 1});
    cout << solution.findMin(v) << endl;
}