#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        if (numRows == 1)
        {
            return vector<vector<int>>({{1}});
        }

        if (numRows == 2)
        {
            return vector<vector<int>>({{1}, {1, 1}});
        }

        vector<vector<int>> rows(numRows);
        rows[0] = vector<int>({1});
        rows[1] = vector<int>({1, 1});

        for (int i = 2; i < numRows; i++)
        {
            vector<int> row_i(i + 1);
            row_i[0] = 1;
            row_i[i] = 1;
            for (int j = 1; j < i; j++)
            {
                row_i[j] = rows[i - 1][j - 1] + rows[i - 1][j];
            }
            rows[i] = row_i;
        }
        return rows;
    }
};

int main()
{
    Solution s;
    s.generate(4);
}