#include <bits/stdc++.h>

using namespace std;

/**
 * Recursive version
 * Time complexity O(amount*n) where n is the number of coins
 * Space complexity O(amount*n)
 *
 * This solution use as table a matrix
 */
// class Solution
// {
// public:
//     int d[10000][13];

//     int solve(vector<int> &c, int v, int i)
//     {
//         if (v == 0)
//         {
//             return 0;
//         }

//         if (i < 0 || v < 0)
//         {
//             return INT_MAX;
//         }

//         if (d[v][i] == -1)
//         {
//             int res = INT_MAX, up = v / c[i];

//             for (int j = 0; j <= up; j++)
//             {
//                 int val = solve(c, v - c[i] * j, i - 1);
//                 if (val != INT_MAX)
//                 {
//                     val += j;
//                 }
//                 res = min(res, val);
//             }
//             d[v][i] = res;
//             return res;
//         }
//         else
//         {
//             return d[v][i];
//         }
//     }

//     int coinChange(vector<int> &c, int amount)
//     {
//         memset(d, -1, sizeof(d));
//         int res = solve(c, amount, c.size() - 1);

//         return res == INT_MAX ? -1 : res;
//     }
// };

/**
 * Top down - Recursive version
 * Time complexity O(amount*n) where n is the number of coins
 * Space complexity O(amount*n)
 *
 * This solution use as table a vector<vector<int>>
 */
// class Solution
// {
// public:
//     vector<vector<int>> d;

//     int solve(vector<int> &c, int v, int i)
//     {
//         if (v == 0)
//         {
//             return 0;
//         }

//         if (i < 0 || v < 0)
//         {
//             return INT_MAX;
//         }

//         if (d[v][i] == -1)
//         {
//             int res = INT_MAX, up = v / c[i];

//             for (int j = 0; j <= up; j++)
//             {
//                 int val = solve(c, v - c[i] * j, i - 1);
//                 if (val != INT_MAX)
//                 {
//                     val += j;
//                 }
//                 res = min(res, val);
//             }
//             d[v][i] = res;
//             return res;
//         }
//         else
//         {
//             return d[v][i];
//         }
//     }

//     int coinChange(vector<int> &c, int amount)
//     {
//         d.resize(amount + 1, vector<int>(c.size(), -1));
//         int res = solve(c, amount, c.size() - 1);

//         return res == INT_MAX ? -1 : res;
//     }
// };

/**
 * Bottom up
 * Time complexity O(amount*n) where n is the number of coins
 * Space complexity O(amount*n)
 *
 * d[v][i] = # of coins needed to add up v considering the coins in c[0],c[1],..,c[i]
 *
 * d[v][i] = min(d[v-c[i]*j][i-1]+j)    with j = 0,...,v/c[i]
 *         = 0                          if v = 0
 *         = v / c[i]                   if i = 0 and v % c[i] == 0
 *         = -1                         if i = 0 and v % c[i] != 0
 */
// class Solution
// {
// public:
//     int coinChange(vector<int> &c, int amount)
//     {
//         vector<vector<int>> d;
//         d.resize(amount + 1, vector<int>(c.size(), amount + 1));
//         int nc = c.size();

//         // 0-th row
//         for (int i = 0; i < nc; i++)
//         {
//             d[0][i] = 0;
//         }

//         // 0-th col
//         for (int v = 0; v <= amount; v++)
//         {
//             if (v % c[0])
//             {
//                 d[v][0] = -1;
//             }
//             else
//             {
//                 d[v][0] = v / c[0];
//             }
//         }

//         for (int v = 1; v <= amount; v++)
//         {
//             for (int i = 1; i < nc; i++)
//             {
//                 int up = v / c[i], res = amount + 1;
//                 for (int j = 0; j <= up; j++)
//                 {
//                     int row = v - c[i] * j;
//                     res = min(res, d[row][i - 1] + j);
//                 }

//                 d[v][i] = res;
//             }
//         }

//         for (int v = 0; v <= amount; v++)
//         {
//             for (int j = 0; j < nc; j++)
//             {
//                 cout << d[v][j] << " ";
//             }
//             cout << "\n";
//         }

//         return d[amount][nc - 1] == amount + 1 ? -1 : d[amount][nc - 1];
//     }
// };

/**
 * Bottom up solution
 *
 * Time complexity O(amount*cn) where cn is the number of coins
 * Space complexity O(amount)
 * 
 * d[v] = optimal # of coins to sum to v using the coins in the array c; v = 0,...,amount
 * 
 * A_v = { v - c[i] >= 0 | i = 0,...,nc }
 * d[v] = min(d[v-c[i]]) + 1; with i in A_v
 * 
 * If A_amount = {} that means that is not possible to sum up to amount with the given coins.
 * To check whether summing to amount is impossible we can use a sentinel value in the array 
 * initialization d equal to amount + 1
 *
 * NOTE: 
 *  - OPT* < amount+1; 
 *  - OPT*=amount <--> we use only the coin 1.
 * 
 */
class Solution
{
public:
    int coinChange(vector<int> &c, int amount)
    {
        vector<int> d(amount+1,amount+1);
        int nc = c.size();
        d[0] = 0;

        for (int v = 1; v <= amount; v++)
        {
            for (int i = 0; i < nc; i++)
            {
                if (v - c[i] >= 0)
                {
                    d[v] = min(d[v], 1 + d[v - c[i]]);
                }
            }
        }

        return d[amount] == (amount + 1) ? -1 : d[amount];
    }
};

int main()
{
    Solution s;

    vector<int> c({2, 5});

    cout << s.coinChange(c, 7) << endl;
}
