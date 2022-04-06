#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> getRow(int rowIndex)
    {
        vector<int> prev(rowIndex + 1, 1);
        vector<int> curr(rowIndex + 1, 1);

        for (int i = 2; i <= rowIndex; i++)
        {
            for (int j = 1; j < i; j++)
            {
                curr[j] = prev[j - 1] + prev[j];
            }
            prev = curr;
        }
        return curr;
    }
};

int main()
{
    Solution s;
    s.getRow(3);
}