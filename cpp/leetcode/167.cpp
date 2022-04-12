#include <bits/stdc++.h>

using namespace std;

/**
 * Time Complexity O(logn)
 * Space Complexity O(1)
 *
 * This solution uses lower_bound function.
 */
// class Solution
// {
// public:
//     vector<int> twoSum(vector<int> &a, int target)
//     {
//         int n = a.size();
//         vector<int> res(2);
//         for (int i = 0; i < n - 1; i++)
//         {
//             int to_find = target - a[i];
//             int lb = lower_bound(a.begin() + i + 1, a.end(), to_find) - a.begin();

//             if (lb < n && a[lb] == to_find)
//             {
//                 res[0] = i + 1;
//                 res[1] = lb + 1;
//                 break;
//             }
//         }

//         return res;
//     }
// };

/**
 * Time Complexity O(logn)
 * Space Complexity O(1)
 *
 * This solution implements binary search.
 */
// class Solution
// {
// public:
//     int search(vector<int> &a, int l, int r, int target)
//     {
//         while (l <= r)
//         {
//             int m = l + (r - l) / 2;
//             if (a[m] == target)
//             {
//                 return m;
//             }

//             if (a[m] < target)
//             {
//                 l = m + 1;
//             }
//             else
//             {
//                 r = m - 1;
//             }
//         }

//         return -1;
//     }

//     vector<int> twoSum(vector<int> &a, int target)
//     {
//         int n = a.size();
//         vector<int> res(2);
//         for (int i = 0; i < n - 1; i++)
//         {
//             int to_find = target - a[i];
//             int lb = search(a, i + 1, n - 1, to_find);

//             if (lb >= 0)
//             {
//                 res[0] = i + 1;
//                 res[1] = lb + 1;
//             }
//         }

//         return res;
//     }
// };

/**
 * Time complexity O(n)
 * Space complexity O(1)
 *
 * Two pointers method.
 */
class Solution
{
public:
    vector<int> twoSum(vector<int> &a, int target)
    {
        int n = a.size();
        vector<int> res(2);

        int l = 0, r = n - 1;

        while (l < r)
        {
            int s = a[l] + a[r];
            if (s > target)
            {
                r--;
            }
            else if (s < target)
            {
                l++;
            }
            else
            {
                res[0] = l + 1;
                res[1] = r + 1;
                return res;
            }
        }

        return res;
    }
};

int main()
{
    vector<int> v({1, 3, 4, 4, 5, 6});
    Solution solution;

    for (int e : solution.twoSum(v, 8))
    {
        cout << e << " ";
    }
}