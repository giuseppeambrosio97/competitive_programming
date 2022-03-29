#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(nlogn) sorting + O(nlogn) DP -> O(nlogn)
 *      But this solution gives TLE
 * Space complexity O(n)
 * */
// class Solution
// {
// public:
//     static bool cmp(vector<int> &l1, vector<int> &l2)
//     {
//         return l1[0] < l2[0];
//     }

//     int find(vector<vector<int>> &intervals, int l, int r, int end)
//     {
//         int mn = r + 1;
//         while (l <= r)
//         {
//             int m = l + (r - l) / 2;
//             if (end <= intervals[m][0])
//             {
//                 mn = min(m, mn);
//                 r = m - 1;
//             }
//             else
//             {
//                 l = m + 1;
//             }
//         }

//         return mn;
//     }

//     int eraseOverlapIntervals(vector<vector<int>> &intervals)
//     {
//         sort(intervals.begin(), intervals.end(), cmp);
//         int n = intervals.size();
//         vector<int> dp(n + 1);

//         int i = n - 1;
//         while (i >= 0)
//         {
//             int j = find(intervals, i, n - 1, intervals[i][1]);

//             dp[i] = max(dp[i + 1], dp[j] + 1);
//             i--;
//         }
//         return n - dp[0];
//     }
// };

/**
 * Time complexity O(nlogn) sorting + O(n) greedy -> O(nlogn)
 * Space complexity O(1)
 * */
class Solution
{
public:
    static bool cmp(vector<int> &l1, vector<int> &l2)
    {
        return (l1[0] < l2[0]) || (l1[0] == l2[0] && l1[1] < l2[1]);
    }

    int eraseOverlapIntervals(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end(), cmp);
        int n = intervals.size(), cnt = 0, end = intervals[0][1];

        for (int i = 1; i < n; i++)
        {
            //not overlapping
            if (end <= intervals[i][0])
            {
                end = intervals[i][1];
            }
            else
            {
                //overlapping
                cnt++;
                //update the new end to the min of the two, doing this we don't need to delete elements
                end = min(end, intervals[i][1]);
            }
        }

        return cnt;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> intervals({{1, 100}, {11, 22}, {1, 11}, {2, 12}});

    cout << s.eraseOverlapIntervals(intervals) << endl;
}