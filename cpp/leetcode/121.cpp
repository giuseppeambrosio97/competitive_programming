#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();

        if (n == 1)
        {
            return 0;
        }

        int best_sale = 0, mx_profit = 0;
        /**
         * At the iteration i we will compute the max profit we can achive if we
         * we buy the stock on day i.
         * */
        for (int i = n - 2; i >= 0; i--)
        {
            best_sale = max(best_sale, prices[i + 1]);
            int best_profit_i = max(best_sale - prices[i], 0);
            mx_profit = max(best_profit_i, mx_profit);
        }
        return mx_profit;
    }

    /**
     * We can use the two pointers method technique. 
     * The two pointers are: L < R
     *      - L = keep track of the minimum price
     *      - R = keep track of the maximum price
     * We iterate through all elements. When we are at the element
     * i what we is: let j an element after i
     *      - a[j] - a[i] will be the eventual revenue
     * CASES:
     *      - a[j] >= a[i] -> update the actual maximum
     *      - a[j] < a[i] -> we can update L because the if the actual max is to buy at day i and
     *                       sell at day j' (with j' < j), and we think that in the future may find a
     *                       better solution what we can say is that if there is a better day, say j'',
     *                       that we buy at day i and sell at day j'' we can say for sure that is better
     *                       to buy in day j and sell in day j''.
     * actual_max = a[j'] - a[i]
     * better_max = a[j''] - a[i]
     * 
     * So a[j''] - a[i] < a[j''] - a[j] because a[j] < a[i]
     * 
     * 
     * */
    int maxProfit2pointersMethod(vector<int> &prices)
    {
        int l = 0, r = 1;
        int profit = 0;

        while (r < prices.size())
        {
            if (prices[l] > prices[r])
            {
                l = r;
            }
            else
            {
                profit = max(profit, prices[r] - prices[l]);
            }
            r++;
        }
        return profit;
    }
};

int main()
{
    Solution s;
    vector<int> v({1, 2});
    cout << s.maxProfit(v) << "\n";
    return 0;
}