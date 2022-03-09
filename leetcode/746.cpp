#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

// class Solution
// {
// public:
//     int minCostClimbingStairs(vector<int> &cost)
//     {
//         int n = cost.size();
//         vector<int> dp(n + 2);
//         dp[n + 1] = 0;
//         dp[n] = 0;
//         for (int i = n - 1; i >= 0; i--)
//         {
//             dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]);
//         }

//         return min(dp[0], dp[1]);
//     }
// };

class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        int n = cost.size();

        for (int i = n - 3; i >= 0; i--)
        {
            cost[i] += min(cost[i + 1], cost[i + 2]);
        }

        return min(cost[0], cost[1]);
    }
};