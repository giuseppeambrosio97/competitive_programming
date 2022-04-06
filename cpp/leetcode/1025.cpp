#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * dp[i][j] = true if player j start with i false otherwise
 * */
// class Solution
// {
// public:
//     bool divisorGame(int n)
//     {
//         vector<vector<bool>> dp(n + 1, vector<bool>(2, false));
//         for (int i = 2; i <= n; i++)
//         {
//             for (int k = 0; k < 2; k++)
//             {
//                 for (int j = 1; j < i; j++)
//                 {
//                     if (i % j == 0)
//                     {
//                         dp[i][k] = dp[i][k] || !dp[i - j][(k + 1) % 2];
//                     }
//                     if (dp[i][k])
//                     {
//                         break;
//                     }
//                 }
//             }
//         }
//         return dp[n][0];
//     }
// };

/**
 * dp[i] = true if the first player win if start with i false otherwise
 * Time complexity O(n^2). Which is exponential because input is a number!
 * */
// class Solution
// {
// public:
//     bool divisorGame(int n)
//     {
//         vector<bool> dp(n + 1, false);
//         for (int i = 2; i <= n; i++)
//         {
//             for (int j = 1; j < i; j++)
//             {
//                 if (i % j == 0)
//                 {
//                     dp[i] = dp[i] || !dp[i - j];
//                 }
//                 if (dp[i])
//                 {
//                     break;
//                 }
//             }
//         }
//         return dp[n];
//     }
// };

/**
 * dp[i] = true if the first player win if start with i false otherwise
 * Time complexity O(n^1.5). Which is exponential because input is a number!
 * */
class Solution
{
public:
    bool divisorGame(int n)
    {
        vector<bool> dp(n + 1, false);
        for (int i = 2; i <= n; i++)
        {
            for (int j = 1; j < sqrt(i); j++)
            {
                if (i % j == 0)
                {
                    dp[i] = dp[i] || !dp[i - j];
                }
                if (dp[i])
                {
                    break;
                }
            }
        }
        return dp[n];
    }
};

/**
 * Time complexity O(1).
 * The first player win if the starting number is even and lose if is odd.
 * 
 * Let's prove this by induction. Proposition to prove:
 *      for each n: P(n): n-1 odd lose -> n even win  
 * BASE STEP : if n = 1: the first player has no move to do, so it will lose.
 * INDUCTIVE STEP :  
 *  Suppose n-1 is odd. If this is true we know that for inductive hypothesis the first player lose.
 *  Let's prove that if n even the first player wins. We know that the first player plays optimally and we know for 
 *  inductive hypothesis that with n-1 the first player loses. So the first player if has n even can choose x = 1 and 
 *  let the second player with n - 1 odd! And we know that if a player start with a odd number he w
 *
 * */
class Solution
{
public:
    bool divisorGame(int n)
    {
        return n % 2;
    }
};

int main()
{
    Solution solution;
    cout << solution.divisorGame(5) << endl;
}
