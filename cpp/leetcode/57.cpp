#include <bits/stdc++.h>

using namespace std;

// class Solution
// {
// public:
//     int find(vector<vector<int>> &intervals, int l, int r, int val)
//     {
//         int mx = -1;
//         while (l <= r)
//         {
//             int m = l + (r - l) / 2;
//             if (intervals[m][0] <= val)
//             {
//                 mx = max(mx, m);
//                 l = m + 1;
//             }
//             else
//             {
//                 r = m - 1;
//             }
//         }
//         return mx;
//     }

//     vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
//     {
//         if (intervals.size() == 0)
//         {
//             intervals.push_back(newInterval);
//             return intervals;
//         }

//         int start = find(intervals, 0, intervals.size() - 1, newInterval[0]);
//         intervals.insert(intervals.begin() + start + 1, newInterval);

//         vector<vector<int>> merged;
//         merged.push_back(intervals[0]);

//         for (int i = 1; i < intervals.size(); i++)
//         {
//             vector<int> *last_interval = &merged.back();
//             if ((*last_interval)[1] >= intervals[i][0])
//             {
//                 (*last_interval)[1] = max((*last_interval)[1], intervals[i][1]);
//             }
//             else
//             {
//                 merged.push_back(intervals[i]);
//             }
//         }

//         return merged;
//     }
// };

class Solution
{
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> merged;

        for (int i = 0; i < intervals.size(); i++)
        {
            if (newInterval[1] < intervals[i][0])
            {
                merged.push_back(newInterval);
                copy(intervals.begin() + i, intervals.end(), back_inserter(merged));
                return merged;
            }
            else if (intervals[i][1] < newInterval[0])
            {
                merged.push_back(intervals[i]);
            }
            else
            {
                newInterval[0] = min(newInterval[0], intervals[i][0]);
                newInterval[1] = max(newInterval[1], intervals[i][1]);
            }
        }

        merged.push_back(newInterval);

        return merged;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> intervals({{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}});
    vector<int> interval({2, 6});
    // vector<int> interval({11, 11});
    // vector<vector<int>> intervals({{-1, -1}, {0, 2}, {3, 3}, {4, 5}});
    // vector<int> interval({6, 8});
    // vector<vector<int>> intervals({{1, 5}});
    // vector<int> interval({0, 5});
    // vector<vector<int>> intervals({{1, 5}});
    // vector<int> interval({6, 8});
    // vector<vector<int>> intervals({{0, 5}, {9, 12}});
    // vector<int> interval({-1, 16});

    for (vector<int> interval : s.insert(intervals, interval))
    {
        cout << interval[0] << " " << interval[1] << endl;
    }
}