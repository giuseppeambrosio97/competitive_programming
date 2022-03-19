#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int countSubstrings(string s)
    {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for (int i = 0; i < n; i++)
        {
            dp[i][i] = true;
        }
        int count = n;

        for (int len = 1; len < n; len++)
        {
            for (int i = 0; i + len < n; i++)
            {
                dp[i][i + len] = s[i] == s[i + len] && (len > 1 ? dp[i + 1][i + len - 1] : true);
                if (dp[i][i + len])
                {
                    count++;
                }
            }
        }

        return count;
    }
};

int main()
{
    Solution solution;
    string s = "abaa";
    solution.countSubstrings(s);
}