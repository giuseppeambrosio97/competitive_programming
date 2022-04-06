#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int rob_I(vector<int> &nums, int i, int j)
    {
        int prev1 = 0, prev2 = 0;
        //...,prev2,prev1,k,k+1,...j
        for (int k = i; k < j; k++)
        {
            int cur_i = max(prev1, nums[k] + prev2);
            prev2 = prev1;
            prev1 = cur_i;
        }
        return prev1;
    }
    int rob(vector<int> &nums)
    {
        int n = nums.size();

        return n == 1 ? nums[0] : max(rob_I(nums, 0, n - 1), rob_I(nums, 1, n));
    }
};

int main()
{
    Solution solution;
    vector<int> v({1, 2, 3});
    cout << solution.rob(v) << endl;
}
