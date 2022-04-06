#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * Kadane's algorithm
 * Time complexity O(n)
 * */
// class Solution
// {
// public:
//     int maxSubArray(vector<int> &nums)
//     {
//         int sum = 0, mx = INT_MIN;

//         for (int i = 0; i < nums.size(); i++)
//         {
//             sum += nums[i];
//             mx = max(mx, sum);
//             sum = max(sum, 0);
//         }
//         return mx;
//     }
// };

/**
 * Divide and conquer
 * Time complexity O(nlogn)
 * */
class Solution
{
public:
    int mid(vector<int> &nums, int m)
    {
        int mx_left = INT_MIN, sum_left = 0;
        for (int k = m; k >= 0; k--)
        {
            sum_left += nums[k];
            mx_left = max(mx_left, sum_left);
        }

        int mx_right = INT_MIN, sum_right = 0;
        for (int k = m + 1; k < nums.size(); k++)
        {
            sum_right += nums[k];
            mx_right = max(mx_right, sum_right);
        }

        return max(mx_right + mx_left, max(mx_right, mx_left));
    }

    int divide_and_conquer(vector<int> &nums, int l, int r)
    {
        if (l == r)
        {
            return nums[l];
        }

        int m = (l + r) / 2;

        int mx_left = divide_and_conquer(nums, l, m);
        int mx_right = divide_and_conquer(nums, m + 1, r);
        int mx_mid = mid(nums, m);
        return max(max(mx_left, mx_right), mx_mid);
    }

    int maxSubArray(vector<int> &nums)
    {
        return divide_and_conquer(nums, 0, nums.size() - 1);
    }
};

int main()
{
    Solution solution;
    vector<int> v({5, 4, -1, 7, 8});
    // cout << solution.maxSubArray(v) << "\n";
    cout << solution.mid(v, 2) << "\n";
}