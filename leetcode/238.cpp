#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(n)
 * Space complexity O(n)
 * */
class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        /*****
         * prefix[i] = nums[0]*nums[1]*...*nums[i]
         * suffix[i] = nums[i]*nums[i+1]*...*nums[n-1]
         * */
        vector<int> res(n), prefix(n), suffix(n);

        prefix[0] = nums[0];
        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i - 1] * nums[i];
        }

        suffix[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--)
        {
            suffix[i] = suffix[i + 1] * nums[i];
        }

        res[0] = suffix[1];
        res[n - 1] = prefix[n - 2];

        for (int i = 1; i < n - 1; i++)
        {
            res[i] = prefix[i - 1] * suffix[i + 1];
        }

        return res;
    }
};

/**
 * Time complexity O(n)
 * Space complexity O(1) without counting the array result as memory used
 * */
class Solution_constant_space
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> res(n, 1);
        int prod = 1;
        for (int i = 0; i < n; i++)
        {
            res[i] = prod;
            prod *= nums[i];
        }
        prod = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            res[i] *= prod;
            prod *= nums[i];
        }

        return res;
    }
};

int main()
{
    Solution s;
    vector<int> a({-1, 1, 0, -3, 3});
    // for (int e : s.productExceptSelf(a))
    // {
    //     cout << e << " ";
    // }
    Solution_constant_space sc;
    for (int e : sc.productExceptSelf(a))
    {
        cout << e << " ";
    }
}