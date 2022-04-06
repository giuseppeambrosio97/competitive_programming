#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    /**
     * dp[i][j] = len of the common subsequence of the string s_i...s_{ns-1} e t_j...t_{nt-1}
     * eq(i,j) = 1 if s[i] == t[j] else 0
     * 
     * BASE STEP :
     *      dp[n][*] = 0
     *      dp[*][0] = 0
     * 
     * We can imagine this by adding a row at the bottom of the matrix dp with all zeros and a column with all zeros
     * at the right of last column of the matrix dp
     * 
     * REC STEP :
     *      dp[i][j] = max(dp[i+1][j],dp[i][j+1],eq(i,j)+dp[i+1][j+1])
     * 
     * The solution of the problem will be dp[0][0]
     * */
    int longestCommonSubsequence_v2(string s, string t)
    {
        int ns = s.length(), nt = t.length();
        vector<vector<int>> dp(ns + 1, vector<int>(nt + 1, 0));

        for (int i = ns - 1; i >= 0; i--)
        {
            for (int j = nt - 1; j >= 0; j--)
            {
                if (s[i] == t[j])
                {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                }
                else
                {
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }
        return dp[0][0];
    }

    /**
     * dp[i][j] = len of the common subsequence of the string s_0...s_i e t_0...t_j
     * eq(i,j) = 1 if s[i] == t[j] else 0
     * 
     * BASE STEP :
     *      dp[0][0] = eq(0,0)
     * REC STEP :
     *      dp[i][j] = max(dp[i-1][j], dp[i][j-1], eq(i,j)+dp[i-1][j-1])
     * The solution of the problem will be dp[ns-1][nt-1]
     * */
    int longestCommonSubsequence(string s, string t)
    {
        int ns = s.length(), nt = t.length();
        vector<vector<int>> dp(ns, vector<int>(nt, 0));

        dp[0][0] = s[0] == t[0];

        for (int i = 0; i < ns; i++)
        {
            for (int j = 0; j < nt; j++)
            {
                if (i == 0 && j != 0)
                {
                    dp[0][j] = dp[0][j - 1] || s[0] == t[j];
                }
                else if (j == 0 && i != 0)
                {
                    dp[i][0] = dp[i - 1][0] || s[i] == t[0];
                }
                else if (i >= 1 && j >= 1)
                {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                    dp[i][j] = max(dp[i - 1][j - 1] + (s[i] == t[j]), dp[i][j]);
                }
            }
        }

        return dp[ns - 1][nt - 1];
    }
};

int main()
{
    Solution solution;

    cout << solution.longestCommonSubsequence("abcde", "ace") << endl;
}