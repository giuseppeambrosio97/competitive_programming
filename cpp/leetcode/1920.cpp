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
 *
 * We need a way to store two numbers in one location.
 *
 * Example:
 *  a = 5, b = 6 and n = 7... with n the lenght of the array.
 *
 *  a + b*n = 5 + 42 = 47
 *
 *  We can use 47 to re-obtain a = 5 and b = 6.
 *
 *  47 % n = 47 % 7 = 5 = a
 *  47 / n = 47 / 7 = 6 = b
 *
 *  In our case the problem is to performe the operation without extra memory, so in other words
 *  to have the value of both nums[i] and nums[nums[i]] but in only one location.
 *  Cause 0<=nums[i]<n we can use the trick explained before.
 *
 *  With a = nums[i] and b = nums[nums[i]] we can do this!
 * */
class Solution
{
public:
    vector<int> buildArray(vector<int> &nums)
    {
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            // nums[nums[i]] % n instead of simply nums[nums[i]]
            // because nums[j] with j < i can be already changed so.
            // If it is changed by doing % n we get back a.
            // If it is not already changed by doing % n, 
            // since every number is less than n, the result doesnt change.
            nums[i] = nums[i] + (nums[nums[i]] % n) * n;
        }

        for (int i = 0; i < n; i++)
        {
            nums[i] = nums[i] / n;
        }

        return nums;
    }
};