#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    /**
     * Space complexity O(n)
     * */
    int fib_n_space(int n)
    {
        int dp[n + 2];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    /**
     * Space complexity O(1)
     * 
     * */
    int fib(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        if (n == 1)
        {
            return 1;
        }

        int prev1 = 0, prev2 = 1, cur;
        for (int i = 2; i <= n; i++)
        {
            cur = prev1 + prev2;
            prev1 = prev2;
            prev2 = cur;
        }
        return cur;
    }
};

int main()
{
    Solution solution;
    cout << solution.fib(2) << endl;
}