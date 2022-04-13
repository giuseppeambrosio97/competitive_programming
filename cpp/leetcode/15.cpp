#include <bits/stdc++.h>

using namespace std;

/**
 * Brutal forces
 *
 * Time complexity O(n^3)
 * Space complexity O(1)
 *
 */
// class Solution
// {
// public:
//     vector<vector<int>> threeSum(vector<int> &a)
//     {
//         int n = a.size(), prevA = INT_MIN, prevB = INT_MIN;
//         sort(a.begin(), a.end());
//         vector<vector<int>> res;

//         for (int i = 0; i < n; i++)
//         {
//             if (a[i] != prevA)
//             {
//                 for (int j = i + 1; j < n; j++)
//                 {
//                     if (a[j] != prevB)
//                     {
//                         for (int k = j + 1; k < n; k++)
//                         {
//                             if (a[i] + a[j] + a[k] == 0)
//                             {
//                                 vector<int> el(3);
//                                 el[0] = a[i];
//                                 el[1] = a[j];
//                                 el[2] = a[k];
//                                 res.push_back(el);
//                             }
//                         }
//                     }
//                     prevB = a[j];
//                 }
//                 prevA = a[i];
//             }
//         }
//         return res;
//     }
// };

/**
 * Time complexity O(n^2) + O(nlogn) = O(n^2)
 * Space complexity O(1) or O(n) depends on the implementation of sorting step
 */
// class Solution
// {
// public:
//     vector<vector<int>> threeSum(vector<int> &a)
//     {
//         int n = a.size();
//         sort(a.begin(), a.end());
//         vector<vector<int>> res;

//         for (int i = 0; i < n; i++)
//         {
//             if (i > 0 and a[i] == a[i - 1])
//             {
//                 continue;
//             }

//             int l = i + 1, r = n - 1;
//             while (l < r)
//             {
//                 int sum = a[i] + a[l] + a[r];

//                 if (sum > 0)
//                 {
//                     r--;
//                 }
//                 else if (sum < 0)
//                 {
//                     l++;
//                 }
//                 else
//                 {
//                     res.push_back(vector<int> ({a[i], a[l], a[r]}));

//                     l++;
//                     while (a[l] == a[l - 1] and l < r)
//                     {
//                         l++;
//                     }
//                 }
//             }
//         }
//         return res;
//     }
// };

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &a)
    {
        int n = a.size();
        sort(a.begin(), a.end());
        vector<vector<int>> res;

        for (int i = 0; i < n; i++)
        {
            if (i == 0 || a[i] != a[i - 1])
            {
                int l = i + 1, r = n - 1;
                while (l < r)
                {
                    int sum = a[l] + a[r];
                    if (sum > -a[i])
                    {
                        r--;
                    }
                    else if (sum < -a[i])
                    {
                        l++;
                    }
                    else
                    {
                        res.push_back(vector<int>({a[i], a[l], a[r]}));
                        l++;

                        while (a[l] == a[l - 1] && l < r)
                        {
                            l++;
                        }
                    }
                }
            }
        }

        return res;
    }
};

int main()
{
    Solution solution;

    vector<int> v({-1, 0, 1, 2, -1, -4});

    for (auto el : solution.threeSum(v))
    {
        cout << el[0] << " " << el[1] << " " << el[2] << "\n";
    }

    for (auto e : v)
    {
        cout << e << " ";
    }
}