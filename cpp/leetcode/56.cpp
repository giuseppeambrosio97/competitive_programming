#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(nlogn)
 * Space complexity O(n)
 * */
class Solution
{
public:
    static bool cmp(vector<int> l1, vector<int> l2)
    {
        return l1[0] < l2[0];
    }

    vector<vector<int>> merge(vector<vector<int>> intervals)
    {
        sort(intervals.begin(), intervals.end(), cmp);

        vector<vector<int>> merged_intervals;

        merged_intervals.push_back(intervals[0]);

        int i = 0, n = intervals.size();
        while (i < n)
        {
            vector<int> *last_interval = &merged_intervals.back();
            if ((*last_interval)[1] >= intervals[i][0])
            {
                (*last_interval)[1] = max(intervals[i][1], (*last_interval)[1]);
            }
            else
            {
                merged_intervals.push_back(intervals[i]);
            }
            i++;
        }
        return merged_intervals;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> intervals({{1, 3}, {2, 6}, {8, 10}, {15, 18}});

    for (vector<int> i : s.merge(intervals))
    {
        cout << i[0] << " " << i[1] << endl;
    }
}