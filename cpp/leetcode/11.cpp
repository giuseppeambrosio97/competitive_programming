#include <bits/stdc++.h>

using namespace std;

/**
 * Brutal force
 * Time complexity O(n^2)
 * Space complexity O(1)
 *
 */
// class Solution
// {
// public:
//     int maxArea(vector<int> &a)
//     {
//         int n = a.size(), mx = -1;

//         for (int i = 0; i < n; i++)
//         {
//             for (int j = i + 1; j < n; j++)
//             {
//                 mx = max(mx, (j - i) * min(a[i], a[j]));
//             }
//         }
//         return mx;
//     }
// };


/**
 * Brutal force
 * Time complexity O(n)
 * Space complexity O(1)  
 */
class Solution
{
public:
    int maxArea(vector<int> &a)
    {
        int n = a.size(), l = 0, r = n - 1, mx = -1;

        while (l < r)
        {
            mx = max(mx, (r - l) * min(a[l], a[r]));

            if (a[l] < a[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        return mx;
    }
};

int main()
{
    Solution s;
    vector<int> v({1, 8, 6, 2, 5, 4, 8, 3, 7});
    // vector<int> v({1, 1});

    cout << s.maxArea(v) << endl;
}