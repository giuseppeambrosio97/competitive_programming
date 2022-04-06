#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * Recurrence relationship: c(i) = number of 1's in the binary representation of i.
 *      - BASE STEP : 
 *              c(0) = 0
 *      - RECURSIVE STEP :
 *              c(i) = 1 + c(i- 2^floor(log_2 i))
 * 
 * */
class Solution
{
public:
    vector<int> countBits(int n)
    {
        vector<int> dp(n + 1);
        for (int i = 1; i <= n; i++)
        {
            int scale = 1 << (int)log2(i);
            dp[i] = 1 + dp[i - scale];
        }
        return dp;
    }
};

int main()
{
    Solution s;
    vector<int> v = s.countBits(4);

    for (int e : v)
    {
        cout << e << " ";
    }
}