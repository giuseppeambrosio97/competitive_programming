#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(n)
 * Space complexity O(n)
 * */
// class Solution
// {
// public:
//     vector<int> buildArray(vector<int> &nums)
//     {
//         int n = nums.size();
//         vector<int> res(n);

//         for (int i = 0; i < n; i++)
//         {
//             res[i] = nums[nums[i]];
//         }

//         return res;
//     }
// };

/**
 * Time complexity O(n)
 * Space complexity O(1)
 * */
class Solution
{
public:
    vector<int> buildArray(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> res(n);

        for (int i = 0; i < n; i++)
        {
            res[i] = nums[nums[i]];
        }

        return res;
    }
};