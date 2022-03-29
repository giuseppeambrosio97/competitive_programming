#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    /**
     * Time complexity O(n)
     * Space complexity O(n)
     * */
    int rob_v1(vector<int> &nums)
    {
        int n = nums.size();

        vector<int> dp(n + 2, 0);

        for (int i = n - 1; i >= 0; i--)
        {
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1]);
        }

        return dp[0];
    }

    /**
     * Time complexity O(n)
     * Space complexity O(1)
     * */
    int rob(vector<int> &nums)
    {
        int n = nums.size(), prev1 = 0, prev2 = 0;

        // ....,prev2,prev1,i,i+1,...
        for (int i = 0; i < n; i++)
        {
            int curr_i = max(prev1, nums[i] + prev2);
            prev2 = prev1;
            prev1 = curr_i;
        }

        return prev1;
    }
};

int main()
{
    Solution solution;
    vector<int> v({1, 2, 3, 1});
    cout << solution.rob(v) << endl;
}
